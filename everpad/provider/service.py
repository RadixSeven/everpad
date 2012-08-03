import sys
sys.path.append('../..')
from everpad.provider.models import (
    Note, Notebook, Tag, ACTION_CHANGE,
    ACTION_CREATE, ACTION_DELETE,
)
from everpad.provider.tools import get_db_session
from sqlalchemy import or_, and_
from sqlalchemy.orm.exc import NoResultFound
from dbus.exceptions import DBusException
from PySide.QtCore import Signal, QObject
import everpad.basetypes as btype
import dbus
import dbus.service

class ProviderServiceQObject(QObject):
    authenticate_signal = Signal()
    remove_authenticate_signal = Signal()


class ProviderService(dbus.service.Object):

    def __init__(self, *args, **kwargs):
        super(ProviderService, self).__init__(*args, **kwargs)
        self.qobject = ProviderServiceQObject()
        

    @property
    def session(self):
        if not hasattr(self, '_session'):
            self._session = get_db_session()
            Note.session = self._session   # shit shit
        return self._session

    @property
    def sq(self):
        if not hasattr(self, '_sq'):
            self._sq = self.session.query
        return self._sq

    @dbus.service.method(
        "com.everpad.Provider", in_signature='i',
        out_signature=btype.Note.signature,
    )
    def get_note(self, id):
        try:
            return btype.Note.from_obj(self.sq(Note).filter(
                and_(Note.id == id, Note.action != ACTION_DELETE),
            ).one()).struct
        except NoResultFound:
            raise DBusException('Note not found')

    @dbus.service.method(
        "com.everpad.Provider", in_signature='saiai',
        out_signature='a%s' % btype.Note.signature,
    )
    def find_notes(self, words, notebooks, tags):
        filters = []
        if words:
            words = '%' + words.replace(' ', '%') + '%'
            filters.append(or_(  # TODO: use xapian
                Note.title.like(words),
                Note.content.like(words),
            ))
        if notebooks:
            filters.append(
                Note.notebook_id.in_(notebooks),
            )
        if tags:
            filters.append(
                Note.tags.any(Tag.id.in_(tags)),
            )
        return map(
            lambda note: btype.Note.from_obj(note).struct,
            self.sq(Note).filter(and_(
                Note.action != ACTION_DELETE,
            *filters)).all(),
        )   

    @dbus.service.method(
        "com.everpad.Provider", in_signature='',
        out_signature='a%s' % btype.Notebook.signature,
    )
    def list_notebooks(self):
        return map(lambda notebook:
            btype.Notebook.from_obj(notebook).struct,
        self.sq(Notebook).all())

    @dbus.service.method(
        "com.everpad.Provider", in_signature='i',
        out_signature=btype.Notebook.signature,
    )
    def get_notebook(self, id):
        try:
            return btype.Notebook.from_obj(self.sq(Notebook).filter(
                Notebook.id == id,
            ).one()).struct
        except NoResultFound:
            raise DBusException('Notebook does not exist')

    @dbus.service.method(
        "com.everpad.Provider", in_signature='',
        out_signature='a%s' % btype.Tag.signature,
    )
    def list_tags(self):
        return map(lambda tag:
            btype.Tag.from_obj(tag).struct,
        self.sq(Tag).all())

    @dbus.service.method(
        "com.everpad.Provider", 
        in_signature=btype.Note.signature,
        out_signature=btype.Note.signature,
    )
    def create_note(self, data):
        note = Note(
            action=ACTION_CREATE,
        )
        btype.Note.from_tuple(data).give_to_obj(note)
        self.session.add(note)
        self.session.commit()
        return btype.Note.from_obj(note).struct

    @dbus.service.method(
        "com.everpad.Provider", 
        in_signature=btype.Note.signature,
        out_signature=btype.Note.signature,
    )
    def update_note(self, note):
        received_note = btype.Note.from_tuple(note)
        try:
            note = self.sq(Note).filter(
                Note.id == received_note.id,
            ).one()
        except NoResultFound:
            raise DBusException('Note not found')
        received_note.give_to_obj(note)
        if note.action != ACTION_CREATE:
            note.action = ACTION_CHANGE
        self.session.commit()
        return btype.Note.from_obj(note).struct

    @dbus.service.method(
        "com.everpad.Provider", 
        in_signature='i', out_signature='b',
    )
    def delete_note(self, id):
        try:
            self.sq(Note).filter(Note.id == id).one().action = ACTION_DELETE
            self.session.commit()
            return True
        except NoResultFound:
            raise DBusException('Note not found')

    @dbus.service.method(
        "com.everpad.Provider", 
        in_signature=btype.Notebook.signature,
        out_signature=btype.Notebook.signature,
    )
    def create_notebook(self, notebook):
        nb = btype.Notebook.from_tuple(notebook)
        if self.sq(Note).filter(
            Notebook.name == nb.name,
        ).count():
            raise DBusException(
                'Notebook with this name already exist',
            )
        notebook = Notebook(action=ACTION_CREATE)
        nb.give_to_obj(notebook)
        self.session.add(notebook)
        self.session.commit()
        return btype.Notebook.from_obj(notebook).struct

    @dbus.service.method(
        "com.everpad.Provider", 
        in_signature='', out_signature='',
    )
    def authenticate(self):
        self.qobject.authenticate_signal.emit()

    @dbus.service.method(
        "com.everpad.Provider", 
        in_signature='', out_signature='',
    )
    def remove_authentication(self):
        self.qobject.remove_authenticate_signal.emit()
from sqlalchemy import Column, String, Integer, Boolean, LargeBinary, DateTime, \
    ForeignKey, UniqueConstraint, Index, PrimaryKeyConstraint
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from .constants import CONTRACT_TABLENAME, \
    EVENT_TABLENAME, EVENT_NAME_LENGTH, \
    LOG_TABLENAME, \
    TOKEN_TABLENAME

Base = declarative_base()


class Contract(Base):
    """
    Contains contract description information
    """
    __tablename__ = CONTRACT_TABLENAME
    __table_args__ = (UniqueConstraint('address'),)

    id = Column(Integer, primary_key=True)

    address = Column(String, unique=True)

    abi = Column(LargeBinary)

    is_listening = Column(Boolean, default=True)
    last_block = Column(Integer, default=-1)

    events = relationship('Event', back_populates='contract', lazy='dynamic')
    tokens = relationship('Token', back_populates='contract', lazy='dynamic')


class Event(Base):
    """
    Contains event description information
    """
    __tablename__ = EVENT_TABLENAME
    __table_args__ = (UniqueConstraint('contract_id', 'name'),)

    id = Column(Integer, primary_key=True)

    contract_id = Column(Integer, ForeignKey('%s.id' % CONTRACT_TABLENAME))
    contract = relationship('Contract', back_populates='events')

    name = Column(String(EVENT_NAME_LENGTH))

    abi = Column(LargeBinary)

    logs = relationship('Log', back_populates='event', lazy='dynamic')

    def __repr__(self):
        return '<Event %s>' % self.name


class Log(Base):
    """
    Contains information about event logs
    """
    __tablename__ = LOG_TABLENAME
    __table_args__ = (UniqueConstraint('event_id', 'block_number'),)

    id = Column(Integer, primary_key=True)

    event_id = Column(Integer, ForeignKey('%s.id' % EVENT_TABLENAME))
    event = relationship('Event', back_populates='logs')

    block_hash = Column(String)
    block_number = Column(Integer)
    log_index = Column(Integer)

    transaction_hash = Column(String)
    transaction_index = Column(Integer)

    timestamp = Column(DateTime)

    args = Column(LargeBinary)

    def __repr__(self):
        return '<Log id=%s (%s)>' % (self.id, self.event)


class Token(Base):
    """
    Contains token information
    """
    __tablename__ = TOKEN_TABLENAME
    __table_args__ = (
        UniqueConstraint('contract_id', 'certificate_id'),
        Index('owner_index', 'owner'),
    )

    id = Column(Integer, primary_key=True)

    contract_id = Column(Integer, ForeignKey('%s.id' % CONTRACT_TABLENAME))
    certificate_id = Column(String)

    contract = relationship('Contract', back_populates='tokens')

    meta_data = Column(LargeBinary)

    owner = Column(String)

    is_claimed = Column(Boolean, default=False)
    claimer = Column(String)
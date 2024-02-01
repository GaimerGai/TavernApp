"""the whole thing

Revision ID: bf89c0f8480d
Revises: 
Create Date: 2024-01-31 22:54:59.061239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bf89c0f8480d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('profilePictureUrl', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('directMessages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=False),
    sa.Column('senderID', sa.String(length=255), nullable=False),
    sa.Column('receiverID', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['receiverID'], ['users.id'], ),
    sa.ForeignKeyConstraint(['senderID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('servers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profilePictureUrl', sa.String(length=255), nullable=False),
    sa.Column('ownerID', sa.String(length=255), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ownerID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('threads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=False),
    sa.Column('senderID', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['senderID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('channels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('serverID', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['serverID'], ['servers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('serverAdmins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('serverID', sa.String(length=255), nullable=False),
    sa.Column('userID', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['serverID'], ['servers.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=2550), nullable=False),
    sa.Column('channelID', sa.String(length=255), nullable=False),
    sa.Column('senderID', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['channelID'], ['channels.id'], ),
    sa.ForeignKeyConstraint(['senderID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('emoji', sa.String(length=255), nullable=False),
    sa.Column('messageID', sa.String(length=255), nullable=False),
    sa.Column('userID', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['messageID'], ['messages.id'], ),
    sa.ForeignKeyConstraint(['userID'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reactions')
    op.drop_table('messages')
    op.drop_table('serverAdmins')
    op.drop_table('channels')
    op.drop_table('threads')
    op.drop_table('servers')
    op.drop_table('directMessages')
    op.drop_table('users')
    # ### end Alembic commands ###

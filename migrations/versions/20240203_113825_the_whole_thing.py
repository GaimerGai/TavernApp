"""the whole thing

Revision ID: b36b8c2b0a72
Revises:
Create Date: 2024-02-03 11:38:25.423307

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b36b8c2b0a72'
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
    op.create_table('servers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('profilePictureUrl', sa.String(length=255), nullable=False),
    sa.Column('ownerId', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['ownerId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('serverAdmins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('serverId', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['serverId'], ['servers.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('channels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('serverId', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['serverId'], ['servers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('threads',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=False),
    sa.Column('senderId', sa.Integer(), nullable=False),
    sa.Column('serverId', sa.Integer(), nullable=False),
    sa.Column('channelId', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['channelId'], ['channels.id'], ),
    sa.ForeignKeyConstraint(['senderId'], ['users.id'], ),
    sa.ForeignKeyConstraint(['serverId'], ['servers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('messages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=2550), nullable=False),
    sa.Column('channelId', sa.Integer(), nullable=False),
    sa.Column('senderId', sa.Integer(), nullable=False),
    sa.Column('threadId', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['channelId'], ['channels.id'], ),
    sa.ForeignKeyConstraint(['senderId'], ['users.id'], ),
    sa.ForeignKeyConstraint(['threadId'], ['threads.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reactions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('emoji', sa.String(length=255), nullable=False),
    sa.Column('messageId', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['messageId'], ['messages.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('directMessages',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('content', sa.String(length=255), nullable=False),
    sa.Column('senderId', sa.Integer(), nullable=False),
    sa.Column('receiverId', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['receiverId'], ['users.id'], name='fk_directMessages_receiverId_users'),
    sa.ForeignKeyConstraint(['senderId'], ['users.id'], name='fk_directMessages_senderId_users'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('directMessages')
    op.drop_table('reactions')
    op.drop_table('messages')
    op.drop_table('channels')
    op.drop_table('threads')
    op.drop_table('serverAdmins')
    op.drop_table('servers')
    op.drop_table('users')
    # ### end Alembic commands ###

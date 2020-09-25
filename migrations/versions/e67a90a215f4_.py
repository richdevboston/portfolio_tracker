"""empty message

Revision ID: e67a90a215f4
Revises: 643fe7811970
Create Date: 2020-09-23 21:30:24.117122

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e67a90a215f4'
down_revision = '643fe7811970'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trades', sa.Column('date', sa.DateTime(), nullable=True))
    op.add_column('trades', sa.Column('direction', sa.String(length=10), nullable=True))
    op.add_column('trades', sa.Column('fees', sa.Float(), nullable=True))
    op.add_column('trades', sa.Column('id', sa.Integer(), nullable=False))
    op.add_column('trades', sa.Column('price', sa.Float(), nullable=True))
    op.add_column('trades', sa.Column('quantity', sa.Float(), nullable=True))
    op.add_column('trades', sa.Column('ticker', sa.String(length=10), nullable=True))
    op.add_column('trades', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_trades_date'), 'trades', ['date'], unique=False)
    op.create_index(op.f('ix_trades_direction'), 'trades', ['direction'], unique=False)
    op.create_index(op.f('ix_trades_fees'), 'trades', ['fees'], unique=False)
    op.create_index(op.f('ix_trades_price'), 'trades', ['price'], unique=False)
    op.create_index(op.f('ix_trades_quantity'), 'trades', ['quantity'], unique=False)
    op.create_index(op.f('ix_trades_ticker'), 'trades', ['ticker'], unique=False)
    op.create_foreign_key(None, 'trades', 'user', ['user_id'], ['id'])
    op.drop_column('trades', 'Quantity')
    op.drop_column('trades', 'ID')
    op.drop_column('trades', 'Direction')
    op.drop_column('trades', 'Fees')
    op.drop_column('trades', 'USER_ID')
    op.drop_column('trades', 'Ticker')
    op.drop_column('trades', 'Price')
    op.drop_column('trades', 'Date')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('trades', sa.Column('Date', sa.DATETIME(), nullable=True))
    op.add_column('trades', sa.Column('Price', sa.TEXT(), nullable=True))
    op.add_column('trades', sa.Column('Ticker', sa.TEXT(), nullable=True))
    op.add_column('trades', sa.Column('USER_ID', sa.INTEGER(), nullable=True))
    op.add_column('trades', sa.Column('Fees', sa.TEXT(), nullable=True))
    op.add_column('trades', sa.Column('Direction', sa.TEXT(), nullable=True))
    op.add_column('trades', sa.Column('ID', sa.INTEGER(), nullable=False))
    op.add_column('trades', sa.Column('Quantity', sa.TEXT(), nullable=True))
    op.drop_constraint(None, 'trades', type_='foreignkey')
    op.drop_index(op.f('ix_trades_ticker'), table_name='trades')
    op.drop_index(op.f('ix_trades_quantity'), table_name='trades')
    op.drop_index(op.f('ix_trades_price'), table_name='trades')
    op.drop_index(op.f('ix_trades_fees'), table_name='trades')
    op.drop_index(op.f('ix_trades_direction'), table_name='trades')
    op.drop_index(op.f('ix_trades_date'), table_name='trades')
    op.drop_column('trades', 'user_id')
    op.drop_column('trades', 'ticker')
    op.drop_column('trades', 'quantity')
    op.drop_column('trades', 'price')
    op.drop_column('trades', 'id')
    op.drop_column('trades', 'fees')
    op.drop_column('trades', 'direction')
    op.drop_column('trades', 'date')
    # ### end Alembic commands ###
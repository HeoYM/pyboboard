"""empty message

Revision ID: cdc1cc3ed3a3
Revises: b1599902cbdc
Create Date: 2024-06-25 18:34:38.541690

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cdc1cc3ed3a3'
down_revision: Union[str, None] = 'b1599902cbdc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question_userlike',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name=op.f('fk_question_userlike_question_id_question')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_question_userlike_user_id_user')),
    sa.PrimaryKeyConstraint('user_id', 'question_id', name=op.f('pk_question_userlike'))
    )
    op.create_table('answer_userlike',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('answer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['answer_id'], ['answer.id'], name=op.f('fk_answer_userlike_answer_id_answer')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_answer_userlike_user_id_user')),
    sa.PrimaryKeyConstraint('user_id', 'answer_id', name=op.f('pk_answer_userlike'))
    )
    op.drop_table('question_voter')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('question_voter',
    sa.Column('user_id', sa.INTEGER(), nullable=False),
    sa.Column('question_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['question_id'], ['question.id'], name='fk_question_voter_question_id_question'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name='fk_question_voter_user_id_user'),
    sa.PrimaryKeyConstraint('user_id', 'question_id', name='pk_question_voter')
    )
    op.drop_table('answer_userlike')
    op.drop_table('question_userlike')
    # ### end Alembic commands ###

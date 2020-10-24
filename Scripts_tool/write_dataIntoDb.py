import sqlite3
import time


class WriteDataIntoDb:
    current = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    conn = sqlite3.connect('../Django_polls/db.sqlite3')  # 连接数据库
    c = conn.cursor()

    # 通过sql语句写入直接
    def write_questions(self, question_text):
        current_time = self.current
        self.c.execute("INSERT INTO polls_question "
                       "(question_text, pub_date) "
                       f"VALUES ('{question_text}','{current_time}')")

        self.conn.commit()

    def get_question_id(self, question_text):
        self.c.execute("SELECT id FROM polls_question WHERE question_text = '%s'" % question_text)
        res = self.c.fetchall()
        return res[0][0]

    def write_choice(self, answer, question_id, ):
        self.c.execute("INSERT INTO polls_choice "
                       "(choice_text, votes, question_id) "
                       "VALUES ('{0}',0,{1})".format(answer, question_id))

        self.conn.commit()


    def close_db(self):
        self.conn.close()


if __name__ == '__main__':
    write_obj = WriteDataIntoDb()
    # write_obj.write_questions("谁是天下第一？")
    # id = write_obj.get_qustion_id("谁是天下第一？")
    write_obj.write_choice("小李子", 3)  # 第二个参数是问题的id

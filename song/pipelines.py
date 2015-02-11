#-*- coding: utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb

class SongPipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect(user='mysql_id', passwd='mysql_pw', db='mysql_db', host='x.x.x.x', charset='utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

        def process_item(self, item, spider):
            try:
                name, nationality, birthday, birthplace, height, weight, position, currentClub, number = None, None, None, None, None, None, None, None, None
                if 'name' in item:    name = item['name']
                if 'nationality' in item:    nationality = item['nationality']
                if 'birthday' in item:    birthday = item['birthday']
                if 'birthplace' in item:    birthplace = item['birthplace']
                if 'height' in item:    height = item['height']
                if 'weight' in item:    weight = item['weight']
                if 'position' in item:    position = item['position']
                if 'currentClub' in item:    currentClub = item['currentClub']
                if 'number' in item:    number = item['number']
                self.cursor.execute('''INSERT INTO scrapy_football_player (name, nationality, birthday, birthplace, height, weight, position, currentClub, number) VALUES (%s, %s,
     %s, %s, %s, %s, %s, %s, %s)''', (name, nationality, birthday, birthplace, height, weight, position, currentClub, number))
                self.conn.commit()
            except MySQLdb.Error, e:
                print "Error %d: %s" % (e.args[0], e.args[1])
                return item
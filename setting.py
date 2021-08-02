import MySQLdb
db=MySQLdb.connect("localhost", "root", "", "wordpress", charset='utf8' )

# 通过cursor创建游标
cursor = db.cursor()
# 执行数据查询
sql1 = "USE wordpress"
sql2= "INSERT INTO `wp_posts` (`ID`, `post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_excerpt`, `post_status`, `comment_status`, `ping_status`, `post_password`, `post_name`, `to_ping`, `pinged`, `post_modified`, `post_modified_gmt`, `post_content_filtered`, `post_parent`, `guid`, `menu_order`, `post_type`, `post_mime_type`, `comment_count`) VALUES ('11', '1', '2021-07-30 15:57:03', '2021-07-30 15:57:03', '<!-- wp:paragraph -->\r\n<p>内容</p>\r\n<!-- /wp:paragraph -->', '标题', '', 'publish', 'open', 'open', '', '6-revision-v1', '', '', '2021-07-30 15:57:03', '2021-07-30 15:57:03', '', '6', 'http://localhost/?p=11', '0', 'post', '', '0')INSERT INTO `wp_posts` (`ID`, `post_author`, `post_date`, `post_date_gmt`, `post_content`, `post_title`, `post_excerpt`, `post_status`, `comment_status`, `ping_status`, `post_password`, `post_name`, `to_ping`, `pinged`, `post_modified`, `post_modified_gmt`, `post_content_filtered`, `post_parent`, `guid`, `menu_order`, `post_type`, `post_mime_type`, `comment_count`) VALUES ('11', '1', '2021-07-30 15:57:03', '2021-07-30 15:57:03', '<!-- wp:paragraph -->\r\n<p>内容</p>\r\n<!-- /wp:paragraph -->', '标题', '', 'publish', 'open', 'open', '', '6-revision-v1', '', '', '2021-07-30 15:57:03', '2021-07-30 15:57:03', '', '6', 'http://localhost/?p=11', '0', 'post', '', '0'); USE wordpress"
cursor.execute(sql1)
cursor.execute(sql2)

#查询数据库单条数据
result = cursor.fetchone()
print(result)
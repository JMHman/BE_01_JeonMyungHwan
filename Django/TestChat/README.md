user 데이터는 db에 저장하고, 채팅 데이터는 db.sqlite3 파일에 저장해서 개인이 관리하도록 한다

/user_id/user 친구 추가된 유저 데이터로 서버 db에서 db.sqlite3로 가져온다.

/user_id/post  특정 유저 채팅 목록 


post/ 채팅방 유저 토큰 방식으로 특정 유저만 확인 가능(특정 유저에게만 확인 가능하게 하는 기능 찾아봐야함), 최신 업데이트사항(new review) 발생시 상단으로 이동(타임데이터로 정렬하게 하고 리뷰 달릴때마다 새로 업데이트 되게 하면 됨)


review 채팅내용 post 이후에 다는 부분이기 때문에 문장 길이 상관없게만 만들기, 새로운 리뷰가 곧 새로운 포스트의 데이터가 되도록 타임데이터 변경되게 하는법 찾아보기
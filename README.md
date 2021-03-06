Kanban
===

#### Repository Setting
- `$ pip install -r requirements.txt`
- `$ python manage.py makemigrations`
- `$ python manage.py migrate`
- `$ python manage.py loaddata fixtures/*.yaml`
- `$ python manage.py runserver`
- Access to `http://localhost:8000`.


#### 사용된 라이브러리
- Bootstrap 4.1.0
- jQuery 2.2.4
- jQuery-ui 1.10.4

#### 구현된 기능
- 카드를 드래그 & 드랍 방식으로 리스트 사이에서 옮기기. 순서 바꾸기
- 카드가 속한 리스트와 순서를 하나의 JSON 배열로 만들고 그 데이터를 DB에 ajax로 입출력
- List에 대한 드래그 & 드랍 방식의 순서 바꾸기
- printLists: 리스트 데이터를 화면에 렌더링
- printCards: 카드 데이터를 카드가 속한 각 리스트에 렌더링
- printUsers: 유저 데이터를 유저가 속한 각 카드에 렌더링

#### 구현해야 할 기능 1
- List에 대한 Create, Edit, Delete
- Card에 대한 Create, Edit, Delete
- User에 대한 Create, Edit, Delete (회원가입, 프로필 수정, 회원탈퇴)
- (List에 대한 Create, Edit 그리고 Card에 대한 Create는 해당 텍스트나 버튼을 클릭하면 바로 텍스트 수정하고 ajax로 전송되도록 구현)
- (List/Card에 대한 Delete는 삭제 버튼을 클릭하면 바로 텍스트 수정하도록 ajax로 구현)
- (Card에 대한 Edit form 입력을 통한 POST 전송방식으로 구현하되 ajax)
- (User에 대한 Create, Edit, Delete는 일반적인 form 입력을 통한 POST 전송방식)
- (2일 예상)

#### 구현해야 할 기능 2
- Card에 대한 Edit에서 User 추가/삭제 ajax로 구현
- (0.5일 예상)

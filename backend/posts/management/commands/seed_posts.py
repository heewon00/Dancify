from random import randint, random, choice
from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from django_seed import Seed

from accounts.models import User
from ...models import FreePost, VideoPost, DancerPost


class Command(BaseCommand):
    help = '이 커맨드를 통해 랜덤한 자유 게시판, 영상 자랑 게시판, 댄서 영상 게시판 데이터 생성.'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '--number',
            default=25,
            type=int,
            help='데이터를 얼마나 생성할 것인지 결정'
        )

    def handle(self, *args: Any, **options: Any) -> str | None:
        number = options.get('number')
        seeder = Seed.seeder()

        texts = [
            'basic_wave',
            '소녀시대 - gee',
            '소녀시대 - 소원을 말해봐',
            '소녀시대 - I got a boy',
            '소녀시대 - 라이온 하트',
            '소녀시대 - Mr.Mr',
            '소녀시대 - 파티',
            '레드벨벳 - 파워 업',
        ]

        # 이미지/비디오 링크
        free_image_urls = [
            'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/post-image/dancer1/yellow-g5adb160c8_1280.jpg',
            'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/post-image/user1/labrador-gfca8dd6ef_1280.jpg',
            'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/post-image/user2/old-tree-gda02f5287_1280.jpg',
            'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/post-image/danceable1/postimage1.jpg',
            'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/post-image/danceable1/postimage2.jpg',
            'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/post-image/danceable1/postimage3.jpg',
        ]

        thumbnail_urls = [
            'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/basic_wave-thumbnail.0000000.jpg',  # basic_wave
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-gee-thumbnail.0000000.jpg",  # 소녀시대 - gee
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-genie-thumbnail.0000000.jpg",  # 소녀시대 - 소원을 말해봐
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-i_got_a_boy-thumbnail.0000000.jpg",  # 소녀시대 - I got a boy
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-lion_heart-thumbnail.0000000.jpg",  # 소녀시대 - 라이온 하트
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-mrmr-thumbnail.0000000.jpg",  # 소녀시대 - Mr.Mr
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-party-thumbnail.0000000.jpg",  # 소녀시대 - 파티
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/red_velvet-power_up-thumbnail.0000000.jpg",  # 레드벨벳 - 파워 업
        ]

        video_urls = [
            'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/basic_wave.m3u8',  # basic_wave
            'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-gee.m3u8',  # 소녀시대 - gee
            "https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-genie.m3u8",  # 소녀시대 - 소원을 말해봐
            "https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-i_got_a_boy.m3u8",  # 소녀시대 - I got a boy
            "https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-lion_heart.m3u8",  # 소녀시대 - 라이온 하트
            "https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-mrmr.m3u8",  # 소녀시대 - Mr.Mr
            "https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-party.m3u8",  # 소녀시대 - 파티
            "https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/red_velvet-power_up.m3u8",  # 레드벨벳 - 파워 업
        ]

        keypoints_urls = [
            'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/basic_wave.json',  # basic_wave
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-gee.json",  # 소녀시대 - gee
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-genie.json",  # 소녀시대 - 소원을 말해봐
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-i_got_a_boy.json",  # 소녀시대 - I got a boy
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-lion_heart.json",  # 소녀시대 - 라이온 하트
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-mrmr.json",  # 소녀시대 - Mr.Mr
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-party.json",  # 소녀시대 - 파티
            "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/red_velvet-power_up.json",  # 레드벨벳 - 파워 업
        ]

        group_names = ['르세라핌', '유키스', '아이브', '(여자)아이들',
                       '몬스타엑스', '하이라이트', '뉴진스', '클라씨',
                       '트러블메이커', '트와이스', '워너원', '에스파',
                       '소녀시대', '블랙핑크', '백퍼센트', '비아이지',
                       '빅스타', '라붐', '브레이브걸스', '에이스',
                       'EXID', '스테이씨', '티아라', '미쓰에이']

        # 전체 유저 리스트 (자유 게시판 작성용)
        users = User.objects.all()

        # 자유 게시판 더미데이터 생성
        seeder.add_entity(FreePost, number,
                          {
                              "user": lambda x: choice(users),
                              "title": lambda x: seeder.faker.sentence(nb_words=4, variable_nb_words=True, ext_word_list=None) + choice(group_names),
                              "content": lambda x: seeder.faker.sentence(nb_words=10, variable_nb_words=True, ext_word_list=None),
                              "post_image": lambda x: choice(free_image_urls) if random() > 0.5 else None,
                              "views": lambda x: randint(0, 999)
                          })

        danceable_ids = ['dancable1', 'dancable2', 'user1', 'user2']
        users = User.objects.filter(user_id__in=danceable_ids)

        # 영상 자랑 게시판 더미데이터 생성
        for i in range(2):
            for j in range(7):
                seeder.add_entity(VideoPost, 1,
                                  {
                                      "user": choice(users),
                                      "title": texts[j],
                                      "content": texts[j],
                                      "video": video_urls[j],
                                      "thumbnail": thumbnail_urls[j],
                                      "views": randint(0, 999)
                                  })

        dancer_ids = ['dancer1', 'dancer2', 'dancer3']
        users = User.objects.filter(user_id__in=dancer_ids)

        # 댄서 게시판 더미데이터 생성
        for i in range(7):
            seeder.add_entity(DancerPost, 1,
                              {
                                  "user": choice(users),
                                  "title": texts[i],
                                  "content": texts[i],
                                  "video": video_urls[i],
                                  "thumbnail": thumbnail_urls[i],
                                  "keypoints": keypoints_urls[0],
                                  "genre": 'kpop' if i != 0 else 'basic',
                                  "feedback_price": randint(10, 99) * 1000,
                                  "views": randint(0, 999)
                              })

        seeder.execute()

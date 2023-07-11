from typing import Any
from django.core.management.base import BaseCommand
from django_seed import Seed

from posts.models import DancerPost
from ...models import VideoSection


class Command(BaseCommand):
    help = '이 커맨드를 통해 비디오 섹션 더미데이터 생성.'

    def handle(self, *args: Any, **options: Any) -> str | None:
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

        # 기본 동작
        basic_wave = [
            # 비디오
            [
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/basic_wave.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/basic_wave_1.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/basic_wave_2.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/basic_wave_3.m3u8',
            ],
            # 썸네일
            [
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/basic_wave-thumbnail.0000000.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/basic_wave_1.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/basic_wave_2.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/basic_wave_3.jpg',
            ],
            # 키포인트
            [
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/basic_wave.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/basic_wave_1.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/basic_wave_3.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/basic_wave_2.json',
            ]
        ]

        # 소녀시대 - gee
        gee = [
            # 비디오
            [
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-gee.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-gee_1.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-gee_2.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-gee_3.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-gee_4.m3u8',
            ],
            # 썸네일
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-gee-thumbnail.0000000.jpg",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-gee_1.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-gee_2.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-gee_3.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-gee_4.jpg',
            ],
            # 키포인트
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-gee.json",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-gee_1.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-gee_2.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-gee_3.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-gee_4.json',
            ]
        ]

        # 소녀시대 - 소원을 말해봐
        genie = [
            # 비디오
            [
                "https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-genie.m3u8",
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-genie_1.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-genie_2.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-genie_3.m3u8',
            ],
            # 썸네일
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-genie-thumbnail.0000000.jpg",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-genie_1.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-genie_2.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-genie_3.jpg',
            ],
            # 키포인트
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-genie.json",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-genie_1.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-genie_2.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-genie_3.json',
            ]
        ]

        # 소녀시대 - I got a boy
        I_got_a_boy = [
            # 비디오
            [
                "https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-i_got_a_boy.m3u8",
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-i_got_a_boy_1.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-i_got_a_boy_2.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-i_got_a_boy_3.m3u8',
            ],
            # 썸네일
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-i_got_a_boy-thumbnail.0000000.jpg",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-i_got_a_boy_1.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-i_got_a_boy_2.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-i_got_a_boy_3.jpg',
            ],
            # 키포인트
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-i_got_a_boy.json",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-i_got_a_boy_1.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-i_got_a_boy_2.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-i_got_a_boy_3.json',
            ]
        ]

        # 소녀시대 - 라이온 하트
        lion_heart = [
            # 비디오
            [
                "https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-lion_heart.m3u8",
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-lion_heart_1.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-lion_heart_2.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-lion_heart_3.m3u8',
            ],
            # 썸네일
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-lion_heart-thumbnail.0000000.jpg",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-lion_heart_1.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-lion_heart_2.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-lion_heart_3.jpg',
            ],
            # 키포인트
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-lion_heart.json",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-lion_heart_1.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-lion_heart_2.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-lion_heart_3.json',
            ]
        ]

        # 소녀시대 - 미스터 미스터
        mrmr = [
            # 비디오
            [
                "https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-mrmr.m3u8",
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-mrmr_1.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-mrmr_2.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-mrmr_3.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-mrmr_4.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-mrmr_5.m3u8',
            ],
            # 썸네일
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-mrmr-thumbnail.0000000.jpg",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-mrmr_1.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-mrmr_2.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-mrmr_3.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-mrmr_4.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-mrmr_5.jpg',
            ],
            # 키포인트
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-mrmr.json",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-mrmr_1.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-mrmr_2.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-mrmr_3.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-mrmr_4.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-mrmr_5.json',
            ]
        ]

        # 소녀시대 - 파티
        party = [
            # 비디오
            [
                "https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-party.m3u8",
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-party_1.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-party_2.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-party_3.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/gg-party_4.m3u8',
            ],
            # 썸네일
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-party-thumbnail.0000000.jpg",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-party_1.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-party_2.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-party_3.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/gg-party_4.jpg',
            ],
            # 키포인트
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-party.json",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-party_1.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-party_2.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-party_3.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/gg-party_4.json',
            ]
        ]

        # 레드벨벳 - 파워 업
        power_up = [
            # 비디오
            [
                "https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/red_velvet-power_up.m3u8",
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/red_velvet-power_up_1.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/red_velvet-power_up_2.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/red_velvet-power_up_3.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/red_velvet-power_up_4.m3u8',
                'https://dl3a13mladdm5.cloudfront.net/vod/dancer/ai_hub_data/red_velvet-power_up_5.m3u8',
            ],
            # 썸네일
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/red_velvet-power_up-thumbnail.0000000.jpg",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/red_velvet-power_up_1.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/red_velvet-power_up_2.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/red_velvet-power_up_3.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/red_velvet-power_up_4.jpg',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/thumbnail/ai_hub_data/red_velvet-power_up_5.jpg',
            ],
            # 키포인트
            [
                "https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/red_velvet-power_up.json",
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/red_velvet-power_up_1.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/red_velvet-power_up_2.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/red_velvet-power_up_3.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/red_velvet-power_up_4.json',
                'https://dancify-bucket2.s3.ap-northeast-2.amazonaws.com/key-points/ai_hub_data/red_velvet-power_up_5.json',
            ]
        ]

        musics = [basic_wave, gee, genie, I_got_a_boy, lion_heart, mrmr, party, power_up]

        for idx, music in enumerate(musics):
            try:
                post = DancerPost.objects.get(title=texts[idx])
            except DancerPost.DoesNotExist:
                continue

            for i in range(len(music[0])):
                seeder.add_entity(VideoSection, 1,
                                  {
                                      'dancer_post': post,
                                      'video': music[0][i],
                                      'thumbnail': music[1][i],
                                      'keypoints': music[2][i],
                                      'section_number': i,
                                  })

        seeder.execute()
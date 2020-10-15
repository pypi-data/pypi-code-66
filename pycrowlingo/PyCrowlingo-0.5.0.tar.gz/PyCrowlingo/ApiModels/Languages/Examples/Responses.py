from pydantic import BaseModel


class Detect(BaseModel):
    class Config:
        schema_extra = {
            "example":
                {'sentences': [{'languages_confidence': [{'name': 'français', 'code': 'fr', 'confidence': 98.0}],
                                'text': 'Bonjour, je suis une phrase en français mais le reste est en farsi.'},
                               {'languages_confidence': [{'name': 'persan', 'code': 'fa', 'confidence': 99.0}],
                                'text': 'اخبار متناقض درباره نامه فرمانده آمریکایی در عراق در حالی که وزیر دفاع '
                                        'آمریکا و رییس ستاد مشترک نیروهای مسلح این کشور تاکید دارند که هیچ طرحی برای '
                                        'خروج نیروهای آمریکایی از عراق وجود ندارد اصالت یک نامه از سوی فرمانده '
                                        'آمریکایی نیروهای اتلاف در عراق که طی آن به وزارت دفاع عراق از جابجایی های '
                                        'اولیه برای خروج از عراق اشاره شده تایید شده است.'},
                               {'languages_confidence': [{'name': 'persan', 'code': 'fa', 'confidence': 99.0}],
                                'text': 'نفیسه کوهنورد - خبرنگار بی بی سی می گوید مقام های آمریکایی در ستاد نیروهای '
                                        'ائتلاف اصالت این نامه را تایید کرده اند و ممکن است تناقضات در گفته های مقام '
                                        'های آمریکایی نشان از اختلاف نظر میان فرماندهان پنتاگون باشد.'},
                               {'languages_confidence': [{'name': 'persan', 'code': 'fa', 'confidence': 83.0}],
                                'text': 'شد.'}],
                 'languages_confidence': [{'name': 'persan', 'code': 'fa', 'confidence': 93.0},
                                          {'name': 'français', 'code': 'fr', 'confidence': 6.0}]}}

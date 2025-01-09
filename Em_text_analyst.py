import pandas as pd
import re
from collections import defaultdict
from collections import Counter
#pd.set_option('display.max_rows', None)

file_path = r'D:\textanalyst\em.csv'
data = pd.read_csv(file_path)
emiin_ner = data["Эмийн нэр"]

#жагсаалтаас хамгийн их давтагдсан нэрсall_em_names.xls
df_data = pd.DataFrame(emiin_ner)
most_common_names = df_data["Эмийн нэр"].value_counts()


#Давтамжийг Dataframe болгон хувиргах
most_common_df = most_common_names.reset_index()
most_common_df.columns = ["Эмийн нэр", "Давтамж"]

categories = {
    "Оношлуур":r"\bОношлуур\b|Oношлуур",
    "Эм":r"\bЭм\b|\bэм\b|Антибиотек",
    "Биологийн идэвхт бүтээгдэхүүн":r"Биологийн идэвхт|Биологийн идэвхит|Хүнсний нэмэлт",
    "Эмийн бус бүтээгдэхүүн":r"Тос,нүүрний|Шампунь|Бэлгэвч|Тос, биеийн|Будаг, үсний|Тос, үсний|Маск, үсний|Өмд, эмэгтэй|Байхуу цай|Шүдний оо \
                                     |Нүүр цэвэрлэгч|Чийгшүүлэгч, нүүрний|Живх|Хүүхдийн тэжээл|Cocок|Тоглоом|Чихэр, хүлхдэг|Тос, гарын|Амтат жигнэмэг \
                                     |Угж, хуванцар|Аяга, хуванцар|Хөөс, үсний|Шоколад|Оо, шүдний|Шүдний оо|Угж|Саван, гарын|Сойз, шүдний|Хатуу чихэр|Сав, угжны \
                                     |Сүүн шингэн, нүүрний|Kофе|Ангижруулагч, үсний|Тос, нүүрний|Сүүн шингэн",
    "Бодис, урвалж, уусмал":r"Урвалж|бодис|Уусмал",
    "Эмнэлэгийн хэрэгсэл":r"мэс заслын|Хиймэл үе|Хуруу шилмэс заслын|Хямсаа, мэс заслын|Багаж, суваг өргөсгөгч|Бээлий, үзлэгийн|Гуурс \
    |Даралтны аппарат|Багаж, хямсаа|микроскопын|Багаж, суваг угаагч|Cав, шээсний|Индоцианин мэдрэгч|сорьц хадгалах|үзлэгийн багаж|Цус тогтоогч|пипетик|Ясны|Ялтас|Cамбай \
    |Абуцел​|Катетер|Kатетер,",
    "Тариа":r"Тариа|Tариа,|Тариур",
    "Бусад":r".*"
}

def classify(name):
    # "\u200b" тэмдэгтийг арилгах
    name = re.sub(r"[\u200b]+", "", name)

    # Бүх ангиллыг шалгах
    for category, pattern in categories.items():
        # "Бусад" ангиллыг хамгийн сүүлд шалгана
        if category == "Бусад":
            continue
        # Тохирсон ангилал олдвол буцаана
        if re.search(pattern, name, re.IGNORECASE):
            return category
    # Ямар ч ангилалд тохироогүй бол "Бусад"-д оруулах
    return "Бусад"  # Ямар ч ангилалд тохироогүй бол "Бусад" руу оруулах

most_common_df["Ангилал"] = most_common_df["Эмийн нэр"].apply(classify)

filtered_data = most_common_df[["Эмийн нэр", "Ангилал"]]

df = pd.DataFrame(filtered_data)

next_filter = df[(df["Эмийн нэр"].notna()) & (df["Ангилал"] == "Бусад")]

next_filter.head(1000)

filtered_data.to_excel(r'D:\textanalyst\filtered_data.xlsx', index=False)


word2 = "А​б​у​ц​е​л"
print("Word2:", word2, "| Урт:", len(word2), "| Тэмдэгтүүд:", list(word2))







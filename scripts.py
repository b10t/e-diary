def fix_marks(schoolkid):
    for point in Mark.objects.filter(schoolkid=schoolkid, points__lte=3):
        point.points = 5
        point.save()


def del_chastisements(schoolkid):
    for chastisement in Chastisement.objects.filter(schoolkid=schoolkid):
        chastisement.delete()

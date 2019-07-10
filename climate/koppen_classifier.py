# -*- coding: utf-8 -*-

# https://en.wikipedia.org/wiki/K%C3%B6ppen_climate_classification

def classify(climate_data):
    avg_tmps = climate_data.monthly_avg_tmps
    avg_precips = climate_data.monthly_avg_precips
    annual_tmp = sum(avg_tmps)/12
    annual_precip = sum(avg_precips)
    hemisphere = climate_data.hemisphere

    if hemisphere == 'North':
        # Apr - Sep
        spring_summer_precips = avg_precips[3:8]
        autumn_winter_precips = avg_precips[0:2] + avg_precips[9:11]
    elif hemisphere == 'South':
        # Oct - Mar
        spring_summer_precips = avg_precips[0:2] + avg_precips[9:11]
        autumn_winter_precips = avg_precips[3:8]
    else:
        raise Exception('Invalid hemisphere {hemisphere}'.format(hemisphere=hemisphere))
    spring_summer_precip = sum(spring_summer_precips)

    desert_threshold = annual_tmp * 20
    if spring_summer_precip > (0.70 * annual_precip):
        desert_threshold += 280
    elif spring_summer_precip > (0.30 * annual_precip):
        desert_threshold += 140
    # else: keep current desert_threshold

    first_letter = ''
    second_letter = ''
    third_letter = ''

    if all(map(lambda avg_tmp: avg_tmp > 18, avg_tmps)):
        first_letter = 'A'
        if all(map(lambda avg_precip: avg_precip > 60, avg_precips)):
            second_letter = 'f'
        elif (min(avg_precips) > 0.04 * annual_precip):
            second_letter = 'm'
        else:
            second_letter = 'w' # or 's'
    elif annual_precip < desert_threshold:
        first_letter = 'B'
        if annual_precip < (0.50 * desert_threshold):
            second_letter = 'W'
        else:
            second_letter = 'S'
        if discriminator_C(avg_tmps):
            third_letter = 'h'
        else:
            third_letter = 'k'
    elif any(map(lambda avg_tmp: avg_tmp > 10, avg_tmps)):
        if discriminator_C(avg_tmps):
            first_letter = 'C'
        else:
            first_letter = 'D'
        if discriminator_w(spring_summer_precips, autumn_winter_precips):
            second_letter = 'w'
        elif discriminator_s(spring_summer_precips, autumn_winter_precips):
            second_letter = 's'
        else:
            second_letter = 'f'
        if discriminator_ab(avg_tmps):
            if discriminator_a(avg_tmps):
                third_letter = 'a'
            else:
                third_letter = 'b'
        elif discriminator_d(avg_tmps):
            third_letter = 'd'
        else:
            third_letter = 'c'
    else:
        first_letter = 'E'
        if any(map(lambda avg_tmp: avg_tmp >= 0, avg_tmps)):
            second_letter = 'T'
        else:
            second_letter = 'F'

    return first_letter + second_letter + third_letter

def discriminator_C(avg_tmps):
    return all(map(lambda avg_tmp: avg_tmp >= 0, avg_tmps))

def discriminator_w(spring_summer_precips, autumn_winter_precips):
    max_summer_precip = max(spring_summer_precips)
    min_winter_precip = min(autumn_winter_precips)
    return max_summer_precip >= (10 * min_winter_precip)

def discriminator_s(spring_summer_precips, autumn_winter_precips):
    max_winter_precip = max(autumn_winter_precips)
    min_summer_precip = min(spring_summer_precips)
    return (max_winter_precip >= (3 * min_summer_precip)) and (min_summer_precip < 30)

def discriminator_ab(avg_tmps):
    return len(list(filter(lambda avg_tmp: avg_tmp > 10, avg_tmps))) >= 4

def discriminator_a(avg_tmps):
    return any(map(lambda avg_tmp: avg_tmp > 22, avg_tmps))

def discriminator_d(avg_tmps):
    return any(map(lambda avg_tmp: avg_tmp < -38, avg_tmps))

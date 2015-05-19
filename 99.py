#encoding=utf8

import sys
import phonenumbers
import re
import csv

from phonenumbers import geocoder

def _extract_number(phonenumber):
    return ''.join(re.findall(r'\d+', phonenumber))


def _parse_phonenumber_obj(phonenumber, region='TW'):
    try:
        phonenumber = phonenumbers.parse(phonenumber, region)
        return phonenumber
    except:
        return phonenumber

def _format_phonenumber(phonenumber_obj, case=1):
    if case == 1:
        return phonenumbers.format_number(
                    phonenumber_obj,
                    phonenumbers.PhoneNumberFormat.E164)
    elif case == 2:
        return phonenumbers.format_number(
                    phonenumber_obj,
                    phonenumbers.PhoneNumberFormat.NATIONAL).replace(' ', '')
    elif case == 3:
        return phonenumbers.format_number(
                    phonenumber_obj,
                    phonenumbers.PhoneNumberFormat.mro).replace(' ', '')

def get_csv_file(filename, num_col_index=1, case=1, region='TW'):
    ret_data = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            try:
                # Parse to phonenumber obj
                phonenumber_obj = _parse_phonenumber_obj(row[num_col_index], region)
                # Format number by case
                new_format_number = _format_phonenumber(phonenumber_obj, case)
                # Replace origin number
                row[num_col_index] = str(new_format_number)

                region_code = geocoder.region_code_for_number(phonenumber_obj)

                # Some phonenumer not in same region
                if region == region_code:
                    ret_data.append(row)
            except:
                ret_data.append(row)
                continue

    return ret_data


def out_csv_file(rows, output_filename='result.csv'):
    with open(output_filename, 'wb') as csvfile:
        for row in rows:
            csvfile.writelines('%s\n' % ', '.join(row))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        num_col_index = int(sys.argv[2])
        region = sys.argv[3]
        case = int(sys.argv[4])

        rows = get_csv_file(
            filename,
            num_col_index=num_col_index,
            case=case,
            region=region)

        out_csv_file(rows=rows)

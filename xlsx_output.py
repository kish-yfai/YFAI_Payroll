import os
import xlsxwriter
from tqdm import tqdm
from company_map import *
from sap_map import *
from payroll_codes import *


def generate_xlsx(pay_checks):
    print("Generating the Excel workbooks...")
    current_path = os.path.curdir
    v = 1
    while os.path.exists(current_path + "\payroll_files_v" + str(v)):
        v += 1
    file_path = current_path + "\payroll_files_v" + str(v)
    os.mkdir(file_path)
    check_header = ["Line Type",
                    "Company",
                    "Paycheck Number",
                    "Offcycle Indicator",
                    "Employee ID",
                    "Employee Type",
                    "First Name",
                    "Middle Name",
                    "Last Name",
                    "Check Date",
                    "Cost Center",
                    "Account Code",
                    "Currency",
                    "ADP Code",
                    "ADP Description",
                    "GL Account",
                    "GL Entity",
                    "Amount"]
    earnings_header = ["Job Code",
                       "Job Title",
                       "Beginning Period",
                       "Ending Period",
                       "Hourly Rate",
                       "Hours",
                       "Rate Used"]
    deductions_header = ["401K Election Percentage"]
    tax_header = ["Liability Indicator"]
    # trail_header = ["Net Pay"]
    total_header = (check_header +
                    earnings_header +
                    deductions_header +
                    tax_header)
    used_codes = []
    # [0] == pc code, [1] == row count
    company_flag = False

    for emp in tqdm(pay_checks):
        company = get_company(emp.company)
        check_date = emp.date
        try:
            pc = emp.cost_center[:4]
        except ValueError:
            pc = emp.cost_center
        pc_date = pc + "_" + check_date
        code_list = [pc, company, pc_date]
        if company != "Not Found":
            company_flag = True
        else:
            company_flag = False
        for code in code_list:
            if code == code_list[1] and company_flag is False:
                continue
            if code not in used_codes:
                if code == pc:
                    name_str = "MTD_" + pc
                elif code == company:
                    name_str = "MTD_" + company
                else:
                    name_str = str(code)
                wb = xlsxwriter.Workbook(filename=(file_path + "/" +
                                                   name_str + "_Payroll.xlsx"))
                header_format = wb.add_format({'bold': True,
                                               'align': 'center',
                                               'bg_color': 'green',
                                               'border': True,
                                               'font_color': 'white'})
                ws = wb.add_worksheet(name="Paycheck Summary")
                c = 0
                for i in total_header:
                    ws.write(0, c, i, header_format)
                    c += 1
                r = 1
                for e in pay_checks:
                    if ((code == e.cost_center[:4]) or
                            (code == get_company(e.company)) or
                            (code == e.cost_center[:4] + "_" + e.date)):
                        common_items = [e.company,
                                        e.paycheck_number,
                                        e.offcycle_indicator,
                                        e.employee_id,
                                        e.employee_type,
                                        e.first_name,
                                        e.middle_name,
                                        e.last_name,
                                        e.date,
                                        e.cost_center,
                                        e.account_code,
                                        e.currency]
                        ern_c = len(check_header)
                        for ern in e.earnings:
                            ws.write(r, 0, "ERN")
                            c = 1
                            for i in common_items:
                                ws.write(r, c, i)
                                c += 1
                            ws.write(r, c + 0, ern.earnings_code)
                            ws.write(r, c + 1, ern.earnings_desc)
                            ws.write(r, c + 2,
                                     output_code(ern.earnings_code,
                                                 e.account_code,
                                                 e.employee_type,
                                                 e.co_code,
                                                 False))
                            ws.write(r, c + 3,
                                     output_code(ern.earnings_code,
                                                 e.account_code,
                                                 e.employee_type,
                                                 e.co_code,
                                                 True))
                            ws.write(r, c + 4, ern.total_earnings)
                            ws.write(r, ern_c + 0, ern.job_code)
                            ws.write(r, ern_c + 1, ern.job_title)
                            ws.write(r, ern_c + 2, ern.begin_period)
                            ws.write(r, ern_c + 3, ern.end_period)
                            ws.write(r, ern_c + 4, ern.std_rate)
                            ws.write(r, ern_c + 5, ern.hours)
                            ws.write(r, ern_c + 6, ern.ot_rate)
                            r += 1
                        ded_c = len(check_header) + len(earnings_header)
                        for ded in e.deductions:
                            ws.write(r, 0, "DED")
                            c = 1
                            for i in common_items:
                                ws.write(r, c, i)
                                c += 1
                            ws.write(r, c + 0, ded.deduction_code)
                            ws.write(r, c + 1, ded.deduction_desc)
                            ws.write(r, c + 2,
                                     output_code(ded.deduction_code,
                                                 e.account_code,
                                                 e.employee_type,
                                                 e.co_code,
                                                 False))
                            ws.write(r, c + 3,
                                     output_code(ded.deduction_code,
                                                 e.account_code,
                                                 e.employee_type,
                                                 e.co_code,
                                                 True))
                            ws.write(r, c + 4, ded.total_deductions)
                            ws.write(r, ded_c + 0, ded.election_percent)
                            r += 1
                        tax_c = (len(check_header) +
                                 len(earnings_header) +
                                 len(deductions_header))
                        for tax in e.taxes:
                            ws.write(r, 0, "TAX")
                            c = 1
                            for i in common_items:
                                ws.write(r, c, i)
                                c += 1
                            ws.write(r, c + 0, tax.tax_code)
                            ws.write(r, c + 1, tax.tax_desc)
                            ws.write(r, c + 2,
                                     output_code(tax.tax_code,
                                                 e.account_code,
                                                 e.employee_type,
                                                 e.co_code,
                                                 False))
                            ws.write(r, c + 3,
                                     output_code(tax.tax_code,
                                                 e.account_code,
                                                 e.employee_type,
                                                 e.co_code,
                                                 True))
                            ws.write(r, c + 4, tax.total_taxes)
                            ws.write(r, tax_c + 0, tax.who_paid)
                            r += 1
                        ws.write(r, 0, "NET")
                        c = 1
                        for i in common_items:
                            ws.write(r, c, i)
                            c += 1
                        ws.write(r, c + 4, e.net_pay)
                        r += 1
                used_codes.append(code)
                wb.close()


def output_code(code,
                account_code,
                employee_type,
                co_code,
                co_check=False):
    if get_code(code, True) is True:
        return "Subtotal Account"
    else:
        sap_account = sap_accounts(code,
                                   account_code,
                                   employee_type)
        if sap_account != "Not Found":
            if co_check is True:
                if "company" in sap_account.lower():
                    return co_code
                else:
                    return account_code[5:]
            else:
                return sap_account[:5]
        # elif QAD Account here
        else:
            return "Not Mapped"

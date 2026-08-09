import requests

from configs import config


# TODO сделать хендлер для админа и выводить в сообщение
def deepseek_check_balance():
    TOKEN_DEEPSEEK = config.token_deepseek_key
    if not TOKEN_DEEPSEEK:
        print("Переменная TOKEN_DEEPSEEK не задана")
        return
    resp = requests.get(
        "https://api.deepseek.com/user/balance",
        headers={"Authorization": f"Bearer {TOKEN_DEEPSEEK}"}
    )
    data = resp.json()

    if not data["is_available"]:
        balance_info = "Баланс исчерпан!"
    else:
        balance_info = f"Всего: {
            data['balance_infos'][0]['total_balance']} {
            data['balance_infos'][0]['currency']} \nВыданные кредиты: {
            data['balance_infos'][0]['granted_balance']} {
                data['balance_infos'][0]['currency']}\nПополненные: {
                    data['balance_infos'][0]['topped_up_balance']} {
                        data['balance_infos'][0]['currency']}"
    return balance_info


# if __name__ == '__main__':
#     print(deepseek_check_balance())

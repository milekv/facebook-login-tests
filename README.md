# Testy Logowania na Facebooku  

Ten projekt zawiera zautomatyzowane testy logowania na Facebooku z użyciem **Selenium WebDriver** oraz **Pythona**.  

## 🚀 Scenariusze Testowe  

- **`test_valid_login()`**: Test sprawdzający udane logowanie z prawidłowymi danymi użytkownika.  
- **`test_invalid_login()`**: Test sprawdzający nieudane logowanie z błędnymi danymi użytkownika.  

## ⚠️ Uwagi  

- **Facebook może blokować zautomatyzowane logowania.**  
  Jeśli napotkasz problemy, spróbuj użyć innego konta testowego lub ręcznie rozwiąż CAPTCHA.  
- Kod może wymagać dostosowań w przypadku zmian na stronie Facebooka.  
- Upewnij się, że używasz aktualnej wersji **ChromeDriver**, aby była zgodna z przeglądarką Chrome.  

## 📌 Wymagania  

- Python  
- Selenium  
- ChromeDriver (zgodny z wersją Chrome)  

## 🛠 Instalacja  

```bash
pip install selenium

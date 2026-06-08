# 🎨 Rust UI Fonts & Previews

[![Rust Version](https://img.shields.io/badge/Rust-Game%20Assets-red.svg)](#)
[![Files](https://img.shields.io/badge/Fonts-13%20TTF-blue.svg)](#)
[![Previews](https://img.shields.io/badge/Previews-10%20PNG-green.svg)](#)

В данном репозитории собраны оригинальные файлы шрифтов (`.ttf`) и превью их рендеринга (`.png`), извлеченные из ресурсов (AssetBundles) игры **Rust**. 

Этот ресурс предназначен для разработчиков плагинов (Oxide, Carbon), дизайнеров интерфейсов и администраторов серверов Rust для точного позиционирования, стилизации и использования встроенных игровых шрифтов в кастомных меню (Custom UI / CUI).

---

## 📋 Список шрифтов и оригинальные пути (Asset Paths)

Для использования шрифта в CUI (через JSON или C# CuiHelper) необходимо указывать его **точный внутренний путь к ассету**. Ниже приведена таблица соответствия файлов в этом репозитории и путей в игре:

| Имя файла в репозитории | Оригинальный путь в игре (Asset Path) | Описание стиля |
| :--- | :--- | :--- |
| **PressStart2P-Regular.ttf** | `assets/content/ui/fonts/pressstart2p-regular.ttf` | Ретро-пиксельный 8-битный стиль. |
| **Super Chiby.ttf** | `assets/content/ui/fonts/superchiby/super chiby.ttf` | Игровой мультяшный, округлый шрифт. |
| **PermanentMarker.ttf** | `assets/content/ui/fonts/permanentmarker.ttf` | Шрифт, имитирующий надпись перманентным маркером. |
| **LCD.ttf** | `assets/content/ui/fonts/lcd/lcd.ttf` | Цифровые LCD-индикаторы. |
| **Roboto-Regular.ttf** | `assets/content/ui/fonts/_roboto/roboto-regular.ttf` | Стандартный шрифт Roboto Regular. |
| **RobotoCondensed-Regular.ttf** | `assets/content/ui/fonts/robotocondensed-regular.ttf` | Узкий шрифт Roboto Condensed. |
| **RobotoCondensed-Bold.ttf** | `assets/content/ui/fonts/robotocondensed-bold.ttf` | Жирный узкий шрифт Roboto. |
| **RobotoMono-Regular.ttf** | `assets/content/ui/fonts/robotomono-regular.ttf` | Моноширинный шрифт Roboto. |
| **RobotoMono-Bold.ttf** | `assets/content/ui/fonts/robotomono-bold.ttf` | Жирный моноширинный шрифт Roboto. |
| **NotoEmoji-Regular.ttf** | `assets/content/ui/fonts/_nonenglish/notoemoji-regular.ttf` | Поддержка эмодзи. |
| **NotoSansArabic-Regular.ttf** | `assets/content/ui/fonts/_nonenglish/arabic/notosansarabic-regular.ttf` | Арабская письменность (Regular). |
| **NotoSansArabic-Bold.ttf** | `assets/content/ui/fonts/_nonenglish/arabic/notosansarabic-bold.ttf` | Арабская письменность (Bold). |
| **NotoSansHebrew-Bold.ttf** | `assets/content/ui/fonts/_nonenglish/hebrew/notosanshebrew-bold.ttf` | Иврит (Bold). |

---

## 💻 Примеры использования в CUI

### 1. Пример в JSON-конфиге Oxide CUI
При создании элемента интерфейса типа `CuiLabel`, укажите оригинальный путь в поле `"font"`:

```json
{
  "name": "MyCustomLabel",
  "parent": "MyParentPanel",
  "components": [
    {
      "type": "UnityEngine.UI.Text",
      "text": "ДОБРО ПОЖАЛОВАТЬ НА СЕРВЕР!",
      "fontSize": 20,
      "align": "MiddleCenter",
      "color": "1 1 1 1",
      "font": "assets/content/ui/fonts/permanentmarker.ttf"
    },
    {
      "type": "RectTransform",
      "anchorsMin": "0 0",
      "anchorsMax": "1 1"
    }
  ]
}
```

### 2. Пример в C# коде плагина (Oxide CUI)
Использование через `CuiPlaceholderHelper` или `CuiLabel`:

```csharp
var label = new CuiLabel
{
    Text = {
        Text = "12:34",
        FontSize = 18,
        Align = TextAnchor.MiddleCenter,
        Font = "assets/content/ui/fonts/lcd/lcd.ttf"
    },
    RectTransform = {
        AnchorMin = "0.1 0.1",
        AnchorMax = "0.9 0.9"
    }
};
```

---

## 🛠️ Как использовать файлы из этого репозитория в дизайне (Figma / Photoshop)

Если вы разрабатываете макеты интерфейсов (UI Mockups) на компьютере:
1. Скачайте интересующий `.ttf` файл из этого репозитория.
2. Установите его в вашу операционную систему (дважды кликните по файлу -> «Установить»).
3. Теперь этот шрифт доступен во всех графических редакторах под своим оригинальным названием (например, *Press Start 2P*, *Permanent Marker*, *Super Chiby*).

---

**TEAM_RUST_PLUGINS — TRP Perfect Standard**

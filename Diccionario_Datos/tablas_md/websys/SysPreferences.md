# websys.SysPreferences

> This persistent class is managed exclusively through websys.Preferences.

**Schema:** websys
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* This persistent class is managed exclusively through websys.Preferences.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AppKey | varchar |  |  | NO | String detemining a module or major part of applic... |
| AppSubKey | varchar |  |  | NO | String detemining sub component of a module or maj... |
| Data | varchar |  |  | SI | Preference Data.<br>
The structure of the data is... |
| LinkedTo | varchar |  |  | SI | Used to link old layouts to system models  |
| ObjectReference | varchar |  |  | NO | This is the ID of the referenced object.<br> |
| ObjectType | varchar |  |  | NO | ObjectType.<br>
This is used to determine the typ... |
| ShortDescription | varchar |  |  | SI | Description for layout/column preferences |
| StreamData | longvarchar |  |  | SI | Preference TextRep Data.
This data is only for te... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
# websys.Preferences

> "Generic holder for user, group, site preferences.

**Schema:** websys
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* "Generic holder for user, group, site preferences.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| AppKey | varchar |  |  | NO | String detemining a module or major part of applic... |
| AppSubKey | varchar |  |  | NO | String detemining sub component of a module or maj... |
| ContextRefClass | varchar |  |  | SI | Class name of context object |
| ContextRefId | varchar |  |  | SI | ID of context object |
| ContextRefOID | varchar |  |  | SI | OID of context object if exists |
| Data | varchar |  |  | SI | Preference Data.
The structure of the data is use... |
| LinkedTo | varchar |  |  | SI | Used to link old layouts to system models  |
| ObjectReference | varchar |  |  | NO | This is the ID of the referenced object. |
| ObjectType | varchar |  |  | NO | ObjectType.
This is used to determine the type of... |
| ShortDescription | varchar |  |  | SI | Description for layout/column preferences |
| StreamData | longvarchar |  |  | SI | Preference TextRep Data.
This data is only for te... |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
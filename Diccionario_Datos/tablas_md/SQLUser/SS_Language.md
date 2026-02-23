# SQLUser.SS_Language

**Schema:** SQLUser
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| CTLAN_RowId | bigint | PK |  | NO | - |
| CTLAN_Code | varchar |  |  | NO | Language Code |
| CTLAN_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| CTLAN_Desc | varchar |  |  | NO | Language Description |
| CTLAN_ISOLanguage | varchar |  |  | SI | ISO Language from Language Standard Type |
| CTLAN_OnlineDocLang | varchar |  |  | SI | Online Help Documentation Language Code from Stand... |
| CTLAN_Owner | varchar |  |  | SI | Owner<br>
Site is for any existing data that is c... |
| CTLAN_UseRTL | varchar |  |  | SI | Indicate if the Reading Direction is from Right |
| CTLAN_ZenCode | varchar |  |  | SI | Zen Language Code |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
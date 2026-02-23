# websys.DictionaryTranslated

> Foreign Languuage Translation of dictionary items

**Schema:** websys
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Foreign Languuage Translation of dictionary items

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| Item | bigint |  |  | NO | - |
| LanguageDR | bigint |  | FK | SI | - |
| Phrase | varchar |  |  | SI | - |
| UpdatedDateTime | timestamp |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
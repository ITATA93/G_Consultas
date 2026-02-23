# SQLUser.MRC_EncEntrySection

**Schema:** SQLUser
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Registros Médicos**. Parámetros de historia clínica.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SECT_RowID | bigint | PK |  | NO | - |
| Q79Q1 | - |  |  | SI | Área |
| Q79Q2 | - |  |  | SI | Evaluación |
| Q79Q3 | - |  |  | SI | Comentarios (Texto libre) |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SECT_Code | varchar |  |  | NO | Code |
| SECT_CodeTableTags | varchar |  |  | SI | Code Table Tags |
| SECT_DateFrom | date |  |  | SI | Effective date for the record |
| SECT_DateTo | date |  |  | SI | Last day the record is active  |
| SECT_Desc | varchar |  |  | NO | Description |
| SECT_Owner | varchar |  |  | SI | Code Table Owner |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
# lab.BB_EDNUnit

**Schema:** lab
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio Clínico**. Módulo de gestión de exámenes de laboratorio.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BBEDNU_ParRef | varchar | PK |  | NO | BB_EDN Parent Reference |
| BBEDNU_Data1 | varchar |  |  | SI | Data in BBP_PackDetails format "|" delimited |
| BBEDNU_Data2 | varchar |  |  | SI | Data in BBP_Antigens format "|," delimited |
| BBEDNU_Data3 | varchar |  |  | SI | Data in BBP_PackTags format "|" delimited |
| BBEDNU_OrderNumber | double |  |  | NO | Order Number |
| BBEDNU_Received | varchar |  |  | SI | Received |
| BBEDNU_RowID | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
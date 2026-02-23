# SQLUser.SS_GroupBillEpisodeType

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| BILLEPTYPE_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| BILLEPTYPE_AdmissionType | varchar |  |  | SI | AdmissionType |
| BILLEPTYPE_Childsub | double |  |  | NO | Childsub |
| BILLEPTYPE_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| BILLEPTYPE_DateFrom | date |  |  | SI | Date From |
| BILLEPTYPE_DateTo | date |  |  | SI | Date To |
| BILLEPTYPE_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
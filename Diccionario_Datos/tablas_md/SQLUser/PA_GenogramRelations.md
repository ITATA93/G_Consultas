# SQLUser.PA_GenogramRelations

**Schema:** SQLUser
**Columnas:** 5
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REL_ParRef | varchar | PK |  | NO | PA_Genogram Parent Reference |
| REL_Childsub | double |  |  | NO | Childsub |
| REL_Nok_DR | varchar |  | FK | SI | Des Ref PANok |
| REL_Person_DR | bigint |  | FK | SI | Des Ref PAPerson |
| REL_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
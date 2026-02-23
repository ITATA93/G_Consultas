# SQLUser.PA_WaitingListRefDoc

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFD_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| REFD_Childsub | double |  |  | NO | Childsub |
| REFD_Consent | varchar |  |  | SI | Consent |
| REFD_DateFrom | date |  |  | SI | Date From |
| REFD_DateTo | date |  |  | SI | Date To |
| REFD_RefDocClinic_DR | varchar |  | FK | SI | Des Ref RefDocClinic |
| REFD_RefDoc_DR | bigint |  | FK | SI | Des Ref RefDoc |
| REFD_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
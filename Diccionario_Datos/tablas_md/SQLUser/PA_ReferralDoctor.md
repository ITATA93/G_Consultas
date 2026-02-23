# SQLUser.PA_ReferralDoctor

**Schema:** SQLUser
**Columnas:** 6
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Referencia/Derivación**. Traslados entre servicios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| REFD_ParRef | bigint | PK |  | NO | PA_PatMas Parent Reference |
| REFD_Childsub | double |  |  | NO | Childsub |
| REFD_DateFrom | date |  |  | SI | Date From |
| REFD_DateTo | date |  |  | SI | Date To |
| REFD_RefDoc_DR | bigint |  | FK | SI | Des Ref RefDoc |
| REFD_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
# SQLUser.PA_WaitingListLoc

**Schema:** SQLUser
**Columnas:** 4
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LOC_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| LOC_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| LOC_Childsub | double |  |  | NO | Childsub |
| LOC_RowId | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
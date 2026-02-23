# SQLUser.SS_ProfilePayors

**Schema:** SQLUser
**Columnas:** 8
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Servicios de Sistema**. Configuración interna.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PAY_ParRef | bigint | PK |  | NO | SS_Group Parent Reference |
| PAY_AuxInsType_DR | bigint |  | FK | SI | Des Ref AuxInsType |
| PAY_CTLOC_DR | bigint |  | FK | SI | Des Ref CTLOC |
| PAY_DateFrom | date |  |  | SI | Date From |
| PAY_DateTo | date |  |  | SI | Date To |
| PAY_InsType_DR | bigint |  | FK | SI | Des Ref InsType |
| PAY_RowID | varchar |  |  | NO | - |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
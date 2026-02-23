# SQLUser.PA_VacSched

**Schema:** SQLUser
**Columnas:** 3
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| VACSCHED_RowId | bigint | PK |  | NO | - |
| VACSCHED_PAPMI_DR | bigint |  | FK | SI | Des Ref PAPatMas |
| VACSCHED_VaccSchedule_DR | bigint |  | FK | SI | Des Ref PACVacSched |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
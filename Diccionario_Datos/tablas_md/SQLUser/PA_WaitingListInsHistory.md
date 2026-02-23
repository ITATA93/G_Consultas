# SQLUser.PA_WaitingListInsHistory

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Lista de Espera**. Gestión de pacientes en espera. Histórico de cambios.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INSH_ParRef | bigint | PK |  | NO | PA_WaitingList Parent Reference |
| ID | varchar |  |  | NO | - |
| INSH_Childsub | double |  |  | NO | Childsub |
| INSH_Date | date |  |  | SI | Date |
| INSH_Payor_DR | bigint |  | FK | SI | Payor |
| INSH_Plan_DR | bigint |  | FK | SI | Plan |
| INSH_SecondPayor_DR | bigint |  | FK | SI | Second Payor |
| INSH_SecondPlan_DR | bigint |  | FK | SI | Second Plan |
| INSH_Time | time |  |  | SI | Time |
| INSH_User_DR | bigint |  | FK | SI | User Name |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
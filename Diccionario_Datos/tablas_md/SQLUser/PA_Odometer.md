# SQLUser.PA_Odometer

**Schema:** SQLUser
**Columnas:** 7
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ODOM_RowId | bigint | PK |  | NO | - |
| ODOM_CTCP_DR | varchar |  | FK | SI | Des Ref CTCP |
| ODOM_Date | date |  |  | SI | Date |
| ODOM_EndOdometer | double |  |  | SI | EndOdometer |
| ODOM_StartOdometer | double |  |  | SI | StartOdometer |
| ODOM_TravelTime | varchar |  |  | SI | Travel Time |
| ODOM_User_DR | bigint |  | FK | SI | Des Ref User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
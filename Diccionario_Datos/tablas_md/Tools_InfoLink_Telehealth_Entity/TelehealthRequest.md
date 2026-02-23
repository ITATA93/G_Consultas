# Tools_InfoLink_Telehealth_Entity.TelehealthRequest

**Schema:** Tools_InfoLink_Telehealth_Entity
**Columnas:** 15
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Herramientas de Sistema**. Utilidades de administración y carga de datos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ID | bigint | PK |  | NO | - |
| APIClient | varchar |  |  | SI | - |
| Action | varchar |  |  | NO | - |
| CreateDate | date |  |  | SI | - |
| CreateTime | time |  |  | SI | - |
| Error | varchar |  |  | SI | - |
| NbrOfRetry | integer |  |  | SI | - |
| ProcessDate | date |  |  | SI | - |
| ProcessTime | time |  |  | SI | - |
| RBAppointmentDR | varchar |  | FK | NO | - |
| RawResponse | varchar |  |  | SI | - |
| ResponseDate | date |  |  | SI | - |
| ResponseStatus | varchar |  |  | SI | - |
| ResponseTime | time |  |  | SI | - |
| Status | varchar |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
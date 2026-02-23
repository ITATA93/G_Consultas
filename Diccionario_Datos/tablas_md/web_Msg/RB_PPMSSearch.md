# web_Msg.RB_PPMSSearch

**Schema:** web_Msg
**Columnas:** 12
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| IsFirstSearch | bit |  |  | SI | Is first search -  populate some of these properti... |
| PPMS_Affiliations | varchar |  |  | SI | Affiliations |
| PPMS_DriveTime | double |  |  | SI | Drive Time |
| PPMS_ProviderReason_DR | bigint |  | FK | SI | Provider Preference Reason  |
| PPMS_Reason_DR | bigint |  | FK | SI | Reason for Select |
| PPMS_RowId | varchar |  |  | SI | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
# web_Msg.LBC_BloodProductGroupBloodGroupException

**Schema:** web_Msg
**Columnas:** 11
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBCBPGBGE_Action | varchar |  |  | SI | Action |
| LBCBPGBGE_ParRef | varchar |  |  | SI | Parent Blood Product Group |
| LBCBPGBGE_PatientBloodGroup_DR | bigint |  | FK | SI | Patient Blood Group
Required by User.LBCBloodProd... |
| LBCBPGBGE_RowID | varchar |  |  | SI | - |
| LBCBPGBGE_UnitBloodGroup_DR | bigint |  | FK | SI | Unit Blood Group
Required by User.LBCBloodProduct... |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
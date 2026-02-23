# SQLUser.PA_PayorApprovGroupReqObservation

**Schema:** SQLUser
**Columnas:** 10
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| OBS_ParRef | bigint | PK |  | NO | PA_PayorApprovalGroupRequest Parent Reference |
| OBS_Childsub | double |  |  | NO | Childsub |
| OBS_Date | date |  |  | SI | Date |
| OBS_ObservCode | varchar |  |  | SI | Observation Code |
| OBS_ObservType_DR | bigint |  | FK | SI | Des Ref to BLCObservationType |
| OBS_ObservValue | varchar |  |  | SI | Observation Value |
| OBS_ObservValueMultiLineText | varchar |  |  | SI | Observation Value Multi Line Text |
| OBS_ObservValueText | varchar |  |  | SI | Observation Value Text |
| OBS_RowId | varchar |  |  | NO | - |
| OBS_Time | time |  |  | SI | Time |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
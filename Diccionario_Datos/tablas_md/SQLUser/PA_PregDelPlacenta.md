# SQLUser.PA_PregDelPlacenta

**Schema:** SQLUser
**Columnas:** 38
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| PLAC_ParRef | varchar | PK |  | NO | PA_PregDelivery Parent Reference |
| PLAC_Calcification | varchar |  |  | SI | Calification |
| PLAC_Childsub | double |  |  | NO | Childsub |
| PLAC_Chorionicity_DR | bigint |  | FK | SI | Chorionicity |
| PLAC_Comments | varchar |  |  | SI | Comments |
| PLAC_CordInsertion_DR | bigint |  | FK | SI | Des ref PAC_CordInsertion |
| PLAC_CordLength | double |  |  | SI | Length of cord |
| PLAC_CordTrueKnot | varchar |  |  | SI | True knot |
| PLAC_CordVessels_DR | bigint |  | FK | SI | Des ref PAC_CordVessels |
| PLAC_DelDate | date |  |  | SI | Delivery Date |
| PLAC_DelTime | time |  |  | SI | Delivery Time |
| PLAC_DelType_DR | bigint |  | FK | SI | Delivery Type DR |
| PLAC_ErrorReason_DR | bigint |  | FK | SI | Des Ref Error Reason |
| PLAC_ExpulsionComplic_DR | bigint |  | FK | SI | Des Ref ORCPlacentaExpulsionComplic |
| PLAC_FreeText1 | varchar |  |  | SI | FreeText1 |
| PLAC_FreeText2 | varchar |  |  | SI | FreeText2 |
| PLAC_FreeText3 | varchar |  |  | SI | FreeText3 |
| PLAC_IndicForPathology | varchar |  |  | SI | Indication for Pathology |
| PLAC_Infracts | varchar |  |  | SI | Infracts |
| PLAC_MembraneCond_DR | bigint |  | FK | SI | Membranes condition Des Ref PAC_MembCond |
| PLAC_OthPlacAnom | varchar |  |  | SI | Other Placenta Anomalies |
| PLAC_PlacentaCond_DR | bigint |  | FK | SI | Des Ref Placenta Condition |
| PLAC_PlacentaNo | double |  |  | SI | Placenta number |
| PLAC_PlacentaWeight | double |  |  | SI | Placenta weight |
| PLAC_ReasonToSendPlacenta | varchar |  |  | SI | Reason to Send Placenta to Pathology |
| PLAC_RowId | varchar |  |  | NO | - |
| PLAC_SenttoPathology | varchar |  |  | SI | Sent to Pathology |
| PLAC_Text1 | varchar |  |  | SI | Text1 |
| PLAC_Text2 | varchar |  |  | SI | Text2 |
| PLAC_Text3 | varchar |  |  | SI | Text3 |
| PLAC_TherapyForComplic_DR | bigint |  | FK | SI | Des Ref ORCTherapyforComplications |
| PLAC_UpdateDate | date |  |  | SI | Last Update Date |
| PLAC_UpdateHospital_DR | bigint |  | FK | SI | Last Update Hospital |
| PLAC_UpdateTime | time |  |  | SI | Last Update Time |
| PLAC_UpdateUser_DR | bigint |  | FK | SI | Last Update User |
| PLAC_YesNo1 | varchar |  |  | SI | YesNo1 |
| PLAC_YesNo2 | varchar |  |  | SI | YesNo2 |
| PLAC_YesNo3 | varchar |  |  | SI | YesNo3 |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
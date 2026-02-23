# SQLUser.ARC_PayAgreemDRGDetails

**Schema:** SQLUser
**Columnas:** 84
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Pagos**. Tarifas y facturación. Detalle de la entidad padre.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DET_ParRef | varchar | PK |  | NO | ARC_PayAgreemDRG Parent Reference |
| DET_AverLengthOfStay | double |  |  | SI | Aver Length Of Stay |
| DET_ChargeMVRateEndOfEpis | varchar |  |  | SI | charge MV rate at the end of episode |
| DET_Childsub | double |  |  | NO | Childsub |
| DET_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DET_Contract_DR | bigint |  | FK | SI | Des Ref Contract |
| DET_CreatedDate | date |  |  | SI | Created Date |
| DET_CreatedTime | time |  |  | SI | Created Time |
| DET_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DET_DateFrom | date |  |  | SI | Date From |
| DET_DateTo | date |  |  | SI | Date To |
| DET_EpisBill_DR | bigint |  | FK | SI | Des Ref EpisBill |
| DET_IncludePrivSuppl | varchar |  |  | SI | Include Priv Suppl |
| DET_LSOutlierBenefit | double |  |  | SI | LS Outlier Benefit |
| DET_LSOutlierDays | double |  |  | SI | LS OutlierDays |
| DET_LowerLevelDesc | varchar |  |  | SI | Lower Level Desc |
| DET_MVRate | double |  |  | SI | Mech Vent Rate |
| DET_OvernightFlagfall | double |  |  | SI | Overnight Flagfall |
| DET_OvernightFlagfallMV | double |  |  | SI | Overnight Flagfall MV |
| DET_Price | double |  |  | SI | Price |
| DET_RowId | varchar |  |  | NO | - |
| DET_SameDayCase6HMV | double |  |  | SI | SameDayCase 6 and more HMV |
| DET_SameDayCaseLess6HMV | double |  |  | SI | Same Day Case Less the 6 Hours MV |
| DET_UpdatedDate | date |  |  | SI | Updated Date |
| DET_UpdatedTime | time |  |  | SI | Updated Time |
| DET_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DET_UpperLevelDesc | varchar |  |  | SI | Upper Level Desc |
| Q01 | - |  |  | SI | CIRCUNSTANCIAS |
| Q02 | - |  |  | SI | 1. De Aislamiento |
| Q03 | - |  |  | SI | 2. Momento Elegido |
| Q04 | - |  |  | SI | 3. Precauciones contra rescate |
| Q05 | - |  |  | SI | 4. Actuación para obtener ayuda |
| Q06 | - |  |  | SI | 5. Actos finales en anticipación |
| Q07 | - |  |  | SI | 6. Carta suicida |
| Q08 | - |  |  | SI | AUTOREPORTE |
| Q09 | - |  |  | SI | 7. Letalidad |
| Q10 | - |  |  | SI | 8. Intención declarada |
| Q11 | - |  |  | SI | 9. Premeditación |
| Q12 | - |  |  | SI | 10. Reacción frente al intento |
| Q13 | - |  |  | SI | RIESGO |
| Q14 | - |  |  | SI | 11. Resultado predecible |
| Q15 | - |  |  | SI | 12. Muerte si no recibiera tratamiento médico |
| Q16 | - |  |  | SI | Resultado Escala de Intención Suicida de Pierce |
| Q16ObsDR | - |  |  | SI | Resultado Escala de Intención Suicida de Pierce DR |
| QUESAnaDR | - |  |  | SI | Anaesthesia |
| QUESAnaOperationDR | - |  |  | SI | Operation |
| QUESConsultDR | - |  |  | SI | Consult |
| QUESCopiedComments | - |  |  | SI | Copied Comments |
| QUESCopiedDate | - |  |  | SI | Copied Date |
| QUESCopiedEpDR | - |  |  | SI | Copied Episode |
| QUESCopiedSourceDR | - |  |  | SI | Copied Source DR |
| QUESCopiedTime | - |  |  | SI | Copied Time |
| QUESCopiedUserDR | - |  |  | SI | Copied User |
| QUESCreateDate | - |  |  | SI | Creation Date |
| QUESCreateTime | - |  |  | SI | Creation Time |
| QUESCreateUserDR | - |  |  | SI | Creation User |
| QUESDate | - |  |  | SI | Last Update Date |
| QUESErrorReasonDR | - |  |  | SI | Error Reason |
| QUESFHResidentDR | - |  |  | SI | Resident |
| QUESMRClinicalPathWaysDR | - |  |  | SI | Clinical Pathway |
| QUESNRCarePlanIssuesDR | - |  |  | SI | Nurse Care Plan Issues |
| QUESOEOrdExecDR | - |  |  | SI | Order Execution |
| QUESORPreanaestheticConsultDR | - |  |  | SI | Preanaesthetic Consultation |
| QUESObsEntryDR | - |  |  | SI | Observation Entry |
| QUESOperRoomDR | - |  |  | SI | Operating Room |
| QUESPAAdmDR | - |  |  | SI | Admission |
| QUESPAAdverseEventDR | - |  |  | SI | Adverse Event |
| QUESPAPatMasDR | - |  |  | SI | Patient |
| QUESPAPregnancyDR | - |  |  | SI | Pregnancy |
| QUESPAWaitingListDR | - |  |  | SI | Waiting List |
| QUESPathwayItemDR | - |  |  | SI | Pathway Item |
| QUESPrePostExamOEOrdItemDR | - |  |  | SI | Pre/Post Exam OrdItem |
| QUESRBAppointmentDR | - |  |  | SI | Appointments |
| QUESRBApptOutcomeDR | - |  |  | SI | Appointment Outcome |
| QUESRBApptSlotDR | - |  |  | SI | Appointment Slot |
| QUESReasonForCorrectionDR | - |  |  | SI | Reason for Correction |
| QUESSSUserDefWindowDR | - |  |  | SI | Questionnaire |
| QUESScore | - |  |  | SI | Score |
| QUESSecondUserDR | - |  |  | SI | Second Signature |
| QUESStatusDR | - |  |  | SI | Status |
| QUESTextResultDR | - |  |  | SI | Text Result |
| QUESTime | - |  |  | SI | Last Update Time |
| QUESTransactionDR | - |  |  | SI | Transaction |
| QUESUserDR | - |  |  | SI | Last Update User |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
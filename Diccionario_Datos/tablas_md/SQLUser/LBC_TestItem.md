# SQLUser.LBC_TestItem

**Schema:** SQLUser
**Columnas:** 141
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| LBCTI_RowID | bigint | PK |  | NO | - |
| LBCTI_AdditionalBloodGroupSystem_DR | bigint |  | FK | SI | Additional Blood Group System
This property will ... |
| LBCTI_AllowedCodedResults | varchar |  |  | SI | Allowed Coded Results (for Numeric Type) |
| LBCTI_AlternateCode | varchar |  |  | SI | Alternate Code |
| LBCTI_AlternateDescription | varchar |  |  | SI | Alternate Description |
| LBCTI_AntibodyScreenOutcome | varchar |  |  | SI | Antibody Screen Outcome
Marks the test item as an... |
| LBCTI_Code | varchar |  |  | NO | Code |
| LBCTI_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| LBCTI_CodeTranslated | varchar |  |  | SI | Code Translated |
| LBCTI_ConditionalDecimals | integer |  |  | SI | Conditional Decimals Places |
| LBCTI_ConditionalDecimalsOperator | varchar |  |  | SI | Conditional Decimals Places Operator |
| LBCTI_ConditionalDecimalsValue | varchar |  |  | SI | Conditional Decimals Places Value |
| LBCTI_CreatedDate | date |  |  | SI | Created Date |
| LBCTI_CreatedTime | time |  |  | SI | Created Time |
| LBCTI_CreatedUser_DR | bigint |  | FK | SI | Created User |
| LBCTI_DateFrom | date |  |  | SI | Effective date for the record |
| LBCTI_DateTo | date |  |  | SI | Last day the record is active  |
| LBCTI_Decimals | integer |  |  | SI | Default Decimal Places |
| LBCTI_Desc | varchar |  |  | NO | Description
HTMLTextBox
Uses SQLUPPER Collation ... |
| LBCTI_DescTranslated | varchar |  |  | SI | Desc Translated |
| LBCTI_IncludeInCumulative | varchar |  |  | SI | Include in Cumulative report |
| LBCTI_Owner | varchar |  |  | SI | Owner |
| LBCTI_ResultType_DR | bigint |  | FK | NO | Result Type |
| LBCTI_Units_DR | bigint |  | FK | SI | Units of Measurement |
| LBCTI_UpdatedDate | date |  |  | SI | Updated Date |
| LBCTI_UpdatedTime | time |  |  | SI | Updated Time |
| LBCTI_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| LBCTI_UseForAKIAlert | varchar |  |  | SI | Creatinine result used to calculate AKI alerts
Ma... |
| LBCTI_UseLabSiteAccreditation | varchar |  |  | SI | Use Lab Site Accreditation  |
| Q01 | - |  |  | SI | Fecha de Comienzo de la lesión |
| Q02 | - |  |  | SI | Descripción del mecanismo |
| Q03 | - |  |  | SI | Cirugía |
| Q04 | - |  |  | SI | Inmovilización |
| Q05 | - |  |  | SI | Ubicación e Intensidad |
| Q06 | - |  |  | SI | Palpación |
| Q07 | - |  |  | SI | Factores que lo Inducen |
| Q08 | - |  |  | SI | Factores que lo Aminoran |
| Q09 | - |  |  | SI | Flexión 180 al Inicio |
| Q10 | - |  |  | SI | Flexión 180 al Alta |
| Q11 | - |  |  | SI | Extensión 45 al Inicio |
| Q12 | - |  |  | SI | Extensión 45 al Alta |
| Q13 | - |  |  | SI | Abd. 160-180 al Inicio |
| Q14 | - |  |  | SI | Abd. 160-180 al Alta |
| Q15 | - |  |  | SI | Add. 20 al Inicio |
| Q16 | - |  |  | SI | Rot. Int. 95 al Inicio |
| Q17 | - |  |  | SI | Add. 20 al Alta |
| Q18 | - |  |  | SI | Rot. Int. 95 al Alta |
| Q19 | - |  |  | SI | Rot. Ext. 70 al Inicio |
| Q20 | - |  |  | SI | Rot. Ext. 70 al Alta |
| Q21 | - |  |  | SI | Flexión 150 al Inicio |
| Q22 | - |  |  | SI | Flexión 150 al Alta |
| Q23 | - |  |  | SI | Extensión 0-10 al Inicio |
| Q24 | - |  |  | SI | Prono-Supinación 85-90 al Inicio |
| Q25 | - |  |  | SI | Prono-Supinación 85-90 al Alta |
| Q26 | - |  |  | SI | Extensión 0-10 al Alta |
| Q27 | - |  |  | SI | Flexión 60-80 al Inicio |
| Q28 | - |  |  | SI | Abducción pulgar 70 al Alta |
| Q29 | - |  |  | SI | Extensión 60-90 al Inicio |
| Q30 | - |  |  | SI | Extensión 60-90 al Alta |
| Q31 | - |  |  | SI | Desviación radial 25-30 al Inicio |
| Q32 | - |  |  | SI | Desviación radial 25-30 al Alta |
| Q33 | - |  |  | SI | Desviación cubital 30-40 al Inicio |
| Q34 | - |  |  | SI | Desviación cubital 30-40 al Alta |
| Q35 | - |  |  | SI | Abducción pulgar 70 al Inicio |
| Q36 | - |  |  | SI | Abducción pulgar 70 al Alta |
| Q37 | - |  |  | SI | Flexión MF pulgar 50 al Inicio |
| Q38 | - |  |  | SI | Flexión MF pulgar 50 al Alta |
| Q39 | - |  |  | SI | Flexión interfalangica pulgar 80 al Inicio |
| Q40 | - |  |  | SI | Flexión IFD 100 al Inicio |
| Q41 | - |  |  | SI | Flexión IFP 90 al Inicio |
| Q42 | - |  |  | SI | Flexión MF 90 al Inicio |
| Q43 | - |  |  | SI | Hiperextensión MF 90 al Inicio |
| Q44 | - |  |  | SI | Flexión IFP 90 al Alta |
| Q45 | - |  |  | SI | Flexión MF 90 al Alta |
| Q46 | - |  |  | SI | Flexión IFD 100 al Alta |
| Q47 | - |  |  | SI | Flexión interfalangica pulgar 80 al Alta |
| Q48 | - |  |  | SI | Hiperextensión MF 90 al Alta |
| Q49 | - |  |  | SI | Pruebas Funcionales |
| Q50 | - |  |  | SI | Cicatriz |
| Q51 | - |  |  | SI | Ortesis y/o Prótesis |
| Q52 | - |  |  | SI | Edema |
| Q53 | - |  |  | SI | Color |
| Q54 | - |  |  | SI | Dolor |
| Q55 | - |  |  | SI | Estadio |
| Q56 | - |  |  | SI | Hipertrófica |
| Q57 | - |  |  | SI | Adherida |
| Q58 | - |  |  | SI | Flexible/Rígida |
| Q59 | - |  |  | SI | Flexión 60-80 al Alta |
| Q60 | - |  |  | SI | Mecanismo de Lesión |
| Q61 | - |  |  | SI | Dolor (EVA) |
| Q62 | - |  |  | SI | Rangos Articulares |
| Q63 | - |  |  | SI | Hombro |
| Q64 | - |  |  | SI | Muñeca-Mano |
| Q65 | - |  |  | SI | Codo |
| Q66 | - |  |  | SI | Cicatriz |
| Q67 | - |  |  | SI | A/P |
| Q68 | - |  |  | SI | A/P |
| Q69 | - |  |  | SI | A/P |
| Q70 | - |  |  | SI | A//P |
| Q71 | - |  |  | SI | A/P |
| Q72 | - |  |  | SI | A/P |
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
# SQLUser.ARC_SundryDebtor

**Schema:** SQLUser
**Columnas:** 91
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEB_RowId | bigint | PK |  | NO | - |
| DEB_Address | varchar |  |  | SI | Address |
| DEB_Address2 | varchar |  |  | SI | Address2 |
| DEB_AltAddress | varchar |  |  | SI | Alternate Address |
| DEB_AltAddress2 | varchar |  |  | SI | AltAddress2 |
| DEB_AltCity_DR | bigint |  | FK | SI | Des Ref AltCity |
| DEB_AltName | varchar |  |  | SI | Alternative Name |
| DEB_AltZip_DR | bigint |  | FK | SI | Des REf Zip |
| DEB_CareProv_DR | varchar |  | FK | SI | Des Ref CareProv |
| DEB_City_DR | bigint |  | FK | SI | Des Ref City |
| DEB_Code | varchar |  |  | NO | Code |
| DEB_CreatedDate | date |  |  | SI | Created Date |
| DEB_CreatedTime | time |  |  | SI | Created Time |
| DEB_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEB_DebtorRef | varchar |  |  | SI | DebtorRef |
| DEB_Desc | varchar |  |  | NO | Description |
| DEB_Email | varchar |  |  | SI | Email |
| DEB_Fax | varchar |  |  | SI | Fax |
| DEB_Hospital_DR | bigint |  | FK | SI | Des Ref Hospital |
| DEB_Notes | varchar |  |  | SI | Notes |
| DEB_OutsBalance | double |  |  | SI | Outstanding Balance |
| DEB_Phone | varchar |  |  | SI | Phone |
| DEB_PhoneExt | varchar |  |  | SI | PhoneExt |
| DEB_UpdatedDate | date |  |  | SI | Updated Date |
| DEB_UpdatedTime | time |  |  | SI | Updated Time |
| DEB_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| DEB_Zip_DR | bigint |  | FK | SI | Des Ref Zip |
| Q01 | - |  |  | SI | Criterio |
| Q02 | - |  |  | SI | Criterios |
| Q03 | - |  |  | SI | Dolor articular de extremidades inferiores |
| Q04 | - |  |  | SI | Observación |
| Q05 | - |  |  | SI | Post por endoprótesis de cadera, rodilla |
| Q06 | - |  |  | SI | Observación |
| Q07 | - |  |  | SI | Síndrome post caída |
| Q08 | - |  |  | SI | Observación |
| Q09 | - |  |  | SI | Secuelas de ACV |
| Q10 | - |  |  | SI | Observación |
| Q11 | - |  |  | SI | Amputados |
| Q12 | - |  |  | SI | Observación |
| Q13 | - |  |  | SI | Alteraciones del equilibrio estático y dinámico |
| Q14 | - |  |  | SI | Observación |
| Q15 | - |  |  | SI | Consideraciones |
| Q16 | - |  |  | SI | Indemnidad de extremidades superiores: fuerza musc... |
| Q17 | - |  |  | SI | Observación |
| Q18 | - |  |  | SI | Indemnidad de extramidades superiores: fuerza musc... |
| Q19 | - |  |  | SI | Observación |
| Q20 | - |  |  | SI | Indemnidad de extremidades superiores: control mot... |
| Q21 | - |  |  | SI | Observación |
| Q22 | - |  |  | SI | Cuadros de demencia en etapa inicial requerirán su... |
| Q23 | - |  |  | SI | Observación |
| Q24 | - |  |  | SI | Otras Observaciones |
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
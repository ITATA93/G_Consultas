# SQLUser.ARC_ItemDependent

**Schema:** SQLUser
**Columnas:** 153
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Arquetipo de configuración**. Definición base del sistema. Items/líneas de detalle.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| DEP_ParRef | varchar | PK |  | NO | ARC_ItmMast Parent Reference |
| DEP_ARCIM_DR | varchar |  | FK | SI | Des Ref ARCIM |
| DEP_Childsub | double |  |  | NO | Childsub |
| DEP_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| DEP_CreatedDate | date |  |  | SI | Created Date |
| DEP_CreatedTime | time |  |  | SI | Created Time |
| DEP_CreatedUser_DR | bigint |  | FK | SI | Created User |
| DEP_DateFrom | date |  |  | SI | Date From |
| DEP_DateTo | date |  |  | SI | Date To |
| DEP_Period | varchar |  |  | SI | Period |
| DEP_RowId | varchar |  |  | NO | - |
| DEP_SameResource | varchar |  |  | SI | Same Resource |
| DEP_TimeFrame | double |  |  | SI | TimeFrame |
| DEP_UpdatedDate | date |  |  | SI | Updated Date |
| DEP_UpdatedTime | time |  |  | SI | Updated Time |
| DEP_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| Q01 | - |  |  | SI | Airways |
| Q01ObsDR | - |  |  | SI | Airways DR |
| Q02 | - |  |  | SI | Instrumented |
| Q02ObsDR | - |  |  | SI | Instrumented DR |
| Q03 | - |  |  | SI | Other |
| Q04 | - |  |  | SI | Inspired oxygen |
| Q04ObsDR | - |  |  | SI | Inspired oxygen DR |
| Q05 | - |  |  | SI | Ventilation |
| Q06 | - |  |  | SI | Measured respiratory frequency |
| Q07 | - |  |  | SI | Respirations |
| Q07ObsDR | - |  |  | SI | Respirations DR |
| Q08 | - |  |  | SI | Respiration |
| Q09 | - |  |  | SI | Inspection |
| Q10 | - |  |  | SI | Chest expansion |
| Q10ObsDR | - |  |  | SI | Chest expansion DR |
| Q11 | - |  |  | SI | Accessory muscle use |
| Q12 | - |  |  | SI | Diaphragmatic breathing |
| Q13 | - |  |  | SI | Paradoxical breathing |
| Q14 | - |  |  | SI | Flail chest |
| Q15 | - |  |  | SI | Laterality |
| Q16 | - |  |  | SI | Palpation |
| Q17 | - |  |  | SI | Subcutaneous emphysema |
| Q18 | - |  |  | SI | Parietal haematoma |
| Q19 | - |  |  | SI | Rib fracture evidence |
| Q20 | - |  |  | SI | Auscultation |
| Q21 | - |  |  | SI | Breath sounds |
| Q22 | - |  |  | SI | Absence of breath sounds |
| Q23 | - |  |  | SI | Inspiratory wheezes |
| Q24 | - |  |  | SI | Expiratory wheezes |
| Q25 | - |  |  | SI | Rales |
| Q26 | - |  |  | SI | Ronchi |
| Q27 | - |  |  | SI | Hb oxygen saturation |
| Q27ObsDR | - |  |  | SI | Hb oxygen saturation DR |
| Q28 | - |  |  | SI | Not assessed |
| Q29 | - |  |  | SI | Not assessable |
| Q30 | - |  |  | SI | Capillary refill time |
| Q30ObsDR | - |  |  | SI | Capillary refill time DR |
| Q31 | - |  |  | SI | Systolic blood pressure |
| Q31ObsDR | - |  |  | SI | Systolic blood pressure DR |
| Q32 | - |  |  | SI | Diastolic blood pressure |
| Q32ObsDR | - |  |  | SI | Diastolic blood pressure DR |
| Q33 | - |  |  | SI | Not measured |
| Q34 | - |  |  | SI | Pulse site |
| Q35 | - |  |  | SI | Heart rate |
| Q35ObsDR | - |  |  | SI | Heart rate DR |
| Q36 | - |  |  | SI | Cardiac rhythm |
| Q36ObsDR | - |  |  | SI | Cardiac rhythm DR |
| Q37 | - |  |  | SI | Asystole |
| Q38 | - |  |  | SI | Pulseless electrical activity |
| Q39 | - |  |  | SI | Ventricular fibrillation |
| Q40 | - |  |  | SI | Estimated blood loss |
| Q40ObsDR | - |  |  | SI | Estimated blood loss DR |
| Q41 | - |  |  | SI | IV fluids |
| Q41ObsDR | - |  |  | SI | IV fluids DR |
| Q42 | - |  |  | SI | Diuresis (in past 8 hours) |
| Q43 | - |  |  | SI | State of consciousness |
| Q44 | - |  |  | SI | Coma |
| Q44ObsDR | - |  |  | SI | Coma DR |
| Q45 | - |  |  | SI | Pupils |
| Q46 | - |  |  | SI | Miosis |
| Q47 | - |  |  | SI | Mydriasis |
| Q48 | - |  |  | SI | Anisocoria R > L |
| Q49 | - |  |  | SI | Anisocoria L > R |
| Q50 | - |  |  | SI | Peripheral Nervous System |
| Q51 | - |  |  | SI | Hyposthenia |
| Q52 | - |  |  | SI | Laterality |
| Q53 | - |  |  | SI | Motor deficit |
| Q54 | - |  |  | SI | Level below |
| Q55 | - |  |  | SI | Sensory deficit |
| Q56 | - |  |  | SI | Level below |
| Q57 | - |  |  | SI | Blood glucose |
| Q57ObsDR | - |  |  | SI | Blood glucose DR |
| Q58 | - |  |  | SI | Head |
| Q59 | - |  |  | SI | Neck |
| Q60 | - |  |  | SI | Thorax |
| Q61 | - |  |  | SI | Abdomen |
| Q62 | - |  |  | SI | Pelvis |
| Q63 | - |  |  | SI | Upper extremities |
| Q64 | - |  |  | SI | Lower extremities |
| Q65 | - |  |  | SI | Back |
| Q66 | - |  |  | SI | Time/Kind of last meal |
| Q67 | - |  |  | SI | Type of event |
| Q68 | - |  |  | SI | Accessory muscle use |
| Q69 | - |  |  | SI | Diaphragmatic breathing |
| Q70 | - |  |  | SI | Paradoxical breathing |
| Q71 | - |  |  | SI | Not assessed |
| Q72 | - |  |  | SI | Not assessable |
| Q73 | - |  |  | SI | Not measured |
| Q74 | - |  |  | SI | Asystole |
| Q75 | - |  |  | SI | Pulseless electrical activity |
| Q76 | - |  |  | SI | Ventricular fibrillation |
| Q77 | - |  |  | SI | Miosis |
| Q78 | - |  |  | SI | Anisocoria R > L |
| Q79 | - |  |  | SI | Anisocoria L > R |
| Q80 | - |  |  | SI | Date |
| Q81 | - |  |  | SI | Time |
| Q82 | - |  |  | SI | Mydriasis |
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
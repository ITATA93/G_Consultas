# SQLUser.IN_GdRetItm

**Schema:** SQLUser
**Columnas:** 108
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Incidentes**. Registro de eventos adversos.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| INGRD_INGRR_ParRef | varchar | PK |  | NO | Des Def INGRR |
| INGRD_AdditQty | double |  |  | NO | Additional Qty(for other return UOM) |
| INGRD_Amount | double |  |  | SI | Return Amount |
| INGRD_BAmount | double |  |  | SI | Base Amount  |
| INGRD_CTUOM_DR | bigint |  | FK | SI | Des Ref to CTUOM(Return Unit) |
| INGRD_ChildSub | numeric |  |  | NO | INGRD ChildSub (New Key) |
| INGRD_INCI_DR | bigint |  | FK | SI | Des Ref to INCItm |
| INGRD_INGRI_DR | varchar |  | FK | NO | Des Ref to INGRI |
| INGRD_ItemNotes | varchar |  |  | SI | A text field to allow recording notes for each sel... |
| INGRD_Qty | double |  |  | NO | Return Quantity |
| INGRD_ReasonReturn_DR | bigint |  | FK | SI | Des Ref ReasonReturn |
| INGRD_Remarks | varchar |  |  | SI | Remarks |
| INGRD_RowId | varchar |  |  | NO | - |
| Q01 | - |  |  | SI | Gait |
| Q01N | - |  |  | SI | Gait_Note |
| Q02 | - |  |  | SI | Nystagmus |
| Q02N | - |  |  | SI | Nystagmus_Note |
| Q03 | - |  |  | SI | Cerebellar Function Test |
| Q04 | - |  |  | SI | Past-pointing : Eyes open |
| Q04N | - |  |  | SI | PPEO_Note |
| Q04ObsDR | - |  |  | SI | Past-pointing : Eyes open DR |
| Q05 | - |  |  | SI | Past-pointing : Eyes closed |
| Q05N | - |  |  | SI | PPEC_Note |
| Q05ObsDR | - |  |  | SI | Past-pointing : Eyes closed DR |
| Q06 | - |  |  | SI | Dysdidokinesia |
| Q06N | - |  |  | SI | Dysdidokinesia_Note |
| Q07 | - |  |  | SI | Romberg's Test |
| Q08 | - |  |  | SI | Eyes open |
| Q08N | - |  |  | SI | Romberg eye open_Note |
| Q08ObsDR | - |  |  | SI | Eyes open DR |
| Q09 | - |  |  | SI | Eyes closed |
| Q09N | - |  |  | SI | Romberg eye closed_Note |
| Q09ObsDR | - |  |  | SI | Eyes closed DR |
| Q10 | - |  |  | SI | Unterberger's Test |
| Q11 | - |  |  | SI | Eyes closed |
| Q11N | - |  |  | SI | Eyes closed_Note |
| Q11ObsDR | - |  |  | SI | Eyes closed DR |
| Q12 | - |  |  | SI | Walking in a straight line |
| Q13 | - |  |  | SI | Eyes open |
| Q13N | - |  |  | SI | Eyes open_Note |
| Q13ObsDR | - |  |  | SI | Eyes open DR |
| Q14 | - |  |  | SI | Eyes closed |
| Q14N | - |  |  | SI | Eyes closed_Note |
| Q14ObsDR | - |  |  | SI | Eyes closed DR |
| Q15 | - |  |  | SI | Cranial Nerves |
| Q16 | - |  |  | SI | Cranial Nerves : II to XII |
| Q16N | - |  |  | SI | Cranial Nerves II to XII_Note |
| Q17 | - |  |  | SI | For detailed examination of Cranial Nerves use Neu... |
| Q17A | - |  |  | SI | Use Neurological Examination Form for details |
| Q18 | - |  |  | SI | Corneal Reflex (Cranial Nerve V) - Right |
| Q18N | - |  |  | SI | CR Right_Note |
| Q19 | - |  |  | SI | Corneal Reflex (Cranial Nerve V) - Left |
| Q19N | - |  |  | SI | CR Left_Note |
| Q20 | - |  |  | SI | Positional Test |
| Q21 | - |  |  | SI | Dix-Hallpike : Right |
| Q21N | - |  |  | SI | Dix-Hallpike Right_Note |
| Q22 | - |  |  | SI | Dix-Hallpike : Left |
| Q22N | - |  |  | SI | Dix-Hallpike Left_Note |
| Q23 | - |  |  | SI | Halmagyi Maneuver |
| Q24 | - |  |  | SI | Right |
| Q24N | - |  |  | SI | Right_Note |
| Q25 | - |  |  | SI | Left |
| Q25N | - |  |  | SI | Left_Note |
| Q26 | - |  |  | SI | Hyperventilation |
| Q26N | - |  |  | SI | Hyperventilation_Note |
| Q27 | - |  |  | SI | Inference |
| Q27TxtOnly | - |  |  | SI | Inference Plain Text Only |
| Q47 | - |  |  | SI | Unterberger's Test outcome |
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
# SQLUser.PAC_AmbulanceCompany

**Schema:** SQLUser
**Columnas:** 179
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Configuración de Admisiones**. Parámetros y tipos para módulo de admisión.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| AMBUL_RowId | bigint | PK |  | NO | - |
| AMBUL_Address | varchar |  |  | SI | Address |
| AMBUL_City_DR | bigint |  | FK | SI | Des Ref CTCity |
| AMBUL_Code | varchar |  |  | NO | Code |
| AMBUL_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| AMBUL_CreatedDate | date |  |  | SI | Created Date |
| AMBUL_CreatedTime | time |  |  | SI | Created Time |
| AMBUL_CreatedUser_DR | bigint |  | FK | SI | Created User |
| AMBUL_DateFrom | date |  |  | SI | Date From |
| AMBUL_DateTo | date |  |  | SI | Date To |
| AMBUL_Desc | varchar |  |  | NO | Description |
| AMBUL_Email | varchar |  |  | SI | Email |
| AMBUL_MobilePhone | varchar |  |  | SI | Mobile Phone |
| AMBUL_NationalCode | varchar |  |  | SI | National Code |
| AMBUL_Owner | varchar |  |  | SI | Owner |
| AMBUL_Phone | varchar |  |  | SI | Phone |
| AMBUL_UpdatedDate | date |  |  | SI | Updated Date |
| AMBUL_UpdatedTime | time |  |  | SI | Updated Time |
| AMBUL_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| AMBUL_Zip_DR | bigint |  | FK | SI | Des Ref CTZip |
| ChildQ109DR | - |  |  | SI | Child Reference: Hazardous materials |
| Q1 | - |  |  | SI | Date |
| Q10 | - |  |  | SI | No food and soiled items laying about |
| Q100 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q101 | - |  |  | SI | Date meet |
| Q102 | - |  |  | SI | Is the room temperature between 18℃ to 25℃ |
| Q103 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q104 | - |  |  | SI | Date meet |
| Q105 | - |  |  | SI | Is the medication refrigerator temperature between... |
| Q106 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q107 | - |  |  | SI | Date meet |
| Q108 | - |  |  | SI | Hazardous material identified at patient's room an... |
| Q11 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q110 | - |  |  | SI | Patient family needed supplies |
| Q112 | - |  |  | SI | Responsibe family member |
| Q113 | - |  |  | SI | Signature |
| Q113UDt | - |  |  | SI | Signature Last Updated Date |
| Q113UTm | - |  |  | SI | Signature Last Updated Time |
| Q12 | - |  |  | SI | Date meet |
| Q13 | - |  |  | SI | No presence of infestation of pests |
| Q14 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q15 | - |  |  | SI | Date meet |
| Q15A | - |  |  | SI | Wires and cables across floors where someone can t... |
| Q16 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q17 | - |  |  | SI | Date meet |
| Q18 | - |  |  | SI | Lighting adequate for patient care and comfort |
| Q19 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q2 | - |  |  | SI | Time |
| Q20 | - |  |  | SI | Date meet |
| Q21 | - |  |  | SI | Easy access to patient |
| Q22 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q23 | - |  |  | SI | Date meet |
| Q24 | - |  |  | SI | Hand rails of stairwells |
| Q25 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q26 | - |  |  | SI | Date meet |
| Q27 | - |  |  | SI | For ambulatory patient, clear path to bathroom |
| Q28 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q29 | - |  |  | SI | Date meet |
| Q3 | - |  |  | SI | Housekeeping and environment |
| Q30 | - |  |  | SI | Grab rail for patient in shower / tub |
| Q31 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q32 | - |  |  | SI | Date meet |
| Q33 | - |  |  | SI | Non slip surface in shower / tub |
| Q34 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q35 | - |  |  | SI | Date meet |
| Q36 | - |  |  | SI | Personal |
| Q37 | - |  |  | SI | For bed bound patient on high bed, side rails |
| Q38 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q39 | - |  |  | SI | Date meet |
| Q4 | - |  |  | SI | Floor and stairwells clean and free of clutter |
| Q40 | - |  |  | SI | Restraints used? (Explain rationale) |
| Q41 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q42 | - |  |  | SI | Date meet |
| Q43 | - |  |  | SI | Caregiver using correct body mechanics for transfe... |
| Q44 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q45 | - |  |  | SI | Date meet |
| Q46 | - |  |  | SI | Ambulatory patient wearing safe footwear |
| Q47 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q48 | - |  |  | SI | Date meet |
| Q49 | - |  |  | SI | Patient who is dependent has alarm bell/phone to c... |
| Q5 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q50 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q51 | - |  |  | SI | Date meet |
| Q52 | - |  |  | SI | Medical equipment, supplies and fire safety |
| Q53 | - |  |  | SI | Safe plug for medical equipment |
| Q54 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q55 | - |  |  | SI | Date meet |
| Q56 | - |  |  | SI | Family trained in use and safety of equipment and ... |
| Q57 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q58 | - |  |  | SI | Date meet |
| Q59 | - |  |  | SI | If there is O2 in place, is there a no smoking sig... |
| Q6 | - |  |  | SI | Date meet |
| Q60 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q61 | - |  |  | SI | Date meet |
| Q62 | - |  |  | SI | All equipment: beds, wheelchair etc |
| Q63 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q64 | - |  |  | SI | Date meet |
| Q65 | - |  |  | SI | Can an older adult contact someone in an emergency... |
| Q66 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q67 | - |  |  | SI | Date meet |
| Q68 | - |  |  | SI | Contact person or supplier are identified for any ... |
| Q69 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q7 | - |  |  | SI | Rugs and carpets firmly in place |
| Q70 | - |  |  | SI | Date meet |
| Q71 | - |  |  | SI | Is the water from public service or private? Clean... |
| Q72 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q73 | - |  |  | SI | Date meet |
| Q74 | - |  |  | SI | Heating and air conditioning control are accessibl... |
| Q75 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q76 | - |  |  | SI | Date meet |
| Q77 | - |  |  | SI | Heat-degradable items are identified and stored pr... |
| Q78 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q79 | - |  |  | SI | Date meet |
| Q8 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q80 | - |  |  | SI | Is designated handwashing available? |
| Q81 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q82 | - |  |  | SI | Date meet |
| Q83 | - |  |  | SI | Are emergency numbers posted on or near all teleph... |
| Q84 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q85 | - |  |  | SI | Date meet |
| Q86 | - |  |  | SI | Is there a fire extinguisher in the house? |
| Q87 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q88 | - |  |  | SI | Date meet |
| Q89 | - |  |  | SI | Is the smoke detector installed where recommended?... |
| Q9 | - |  |  | SI | Date meet |
| Q90 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q91 | - |  |  | SI | Date meet |
| Q92 | - |  |  | SI | Is there a fire exit plan prepared and practiced? |
| Q93 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q94 | - |  |  | SI | Date meet |
| Q96 | - |  |  | SI | Medication management |
| Q96A | - |  |  | SI | Medication in date and stored safely away from chi... |
| Q97 | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q97A | - |  |  | SI | What is being done (needs to be done) to meet safe... |
| Q98 | - |  |  | SI | Date meet |
| Q98A | - |  |  | SI | Date meet |
| Q99 | - |  |  | SI | Medication storage within patient reach |
| Q99A | - |  |  | SI | Medication storage within patient reach |
| Q99B | - |  |  | SI | Responsible person identified in medication admini... |
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
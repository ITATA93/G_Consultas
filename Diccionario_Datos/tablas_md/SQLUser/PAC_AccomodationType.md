# SQLUser.PAC_AccomodationType

**Schema:** SQLUser
**Columnas:** 199
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare. Tipos/categorías disponibles.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| ACCOMT_RowId | bigint | PK |  | NO | - |
| ACCOMT_Code | varchar |  |  | NO | Code |
| ACCOMT_CodeTableTags | varchar |  |  | SI | List of code table Tags |
| ACCOMT_CreatedDate | date |  |  | SI | Created Date |
| ACCOMT_CreatedTime | time |  |  | SI | Created Time |
| ACCOMT_CreatedUser_DR | bigint |  | FK | SI | Created User |
| ACCOMT_DateFrom | date |  |  | SI | Date From |
| ACCOMT_DateTo | date |  |  | SI | Date To |
| ACCOMT_Desc | varchar |  |  | NO | Description |
| ACCOMT_NationalCode | varchar |  |  | SI | National Code |
| ACCOMT_Owner | varchar |  |  | SI | Owner |
| ACCOMT_UpdatedDate | date |  |  | SI | Updated Date |
| ACCOMT_UpdatedTime | time |  |  | SI | Updated Time |
| ACCOMT_UpdatedUser_DR | bigint |  | FK | SI | Updated User |
| ACCOMT_WL | varchar |  |  | SI | Waiting List |
| Q01 | - |  |  | SI | SUP, HEAD IN MIDLINE: Turns head with extremities ... |
| Q02 | - |  |  | SI | SUP: Brings hands to midline, fingers one with the... |
| Q03 | - |  |  | SI | SUP: Lifts head 45° |
| Q04 | - |  |  | SI | SUP: Flexes R hip and knee through full range |
| Q05 | - |  |  | SI | SUP: Flexes L hip and knee through full range |
| Q06 | - |  |  | SI | SUP: Reaches out with R arm, hand crosses midline ... |
| Q07 | - |  |  | SI | SUP: Reaches out with L arm, hand crosses midline ... |
| Q08 | - |  |  | SI | SUP: Rolls to PR over R side |
| Q09 | - |  |  | SI | SUP: Rolls to PR over L side |
| Q10 | - |  |  | SI | PR: Lifts head upright |
| Q100 | - |  |  | SI | Testing with aids |
| Q101 | - |  |  | SI | Aid |
| Q102 | - |  |  | SI | Dimensions |
| Q103 | - |  |  | SI | Rollator / pusher |
| Q104 | - |  |  | SI | Rollator  / pusher |
| Q105 | - |  |  | SI | Walker |
| Q106 | - |  |  | SI | Walker dimension |
| Q107 | - |  |  | SI | H frame crutches |
| Q108 | - |  |  | SI | H frame crutches dimension |
| Q109 | - |  |  | SI | Crutches |
| Q11 | - |  |  | SI | PR ON FOREARMS: Lifts head upright, elbows ext, ch... |
| Q110 | - |  |  | SI | Crutches dimensions |
| Q111 | - |  |  | SI | Quad cane |
| Q112 | - |  |  | SI | Quad cane dimension |
| Q113 | - |  |  | SI | Cane |
| Q114 | - |  |  | SI | Cane dimension |
| Q115 | - |  |  | SI | Other |
| Q116 | - |  |  | SI | Other dimension |
| Q117 | - |  |  | SI | Hip control |
| Q118 | - |  |  | SI | Hip control dimension |
| Q119 | - |  |  | SI | Knee control |
| Q12 | - |  |  | SI | PR ON FOREARMS: Weight on R forearm, fully extends... |
| Q120 | - |  |  | SI | Knee control dimension |
| Q121 | - |  |  | SI | Ankle-foot control |
| Q122 | - |  |  | SI | Ankle-foot control dimension |
| Q123 | - |  |  | SI | Foot control |
| Q124 | - |  |  | SI | Foot control dimension |
| Q125 | - |  |  | SI | Shoes |
| Q126 | - |  |  | SI | Shoes dimension |
| Q127 | - |  |  | SI | Other |
| Q128 | - |  |  | SI | Other dimension |
| Q129 | - |  |  | SI | Testing with orthoses |
| Q13 | - |  |  | SI | PR ON FOREARMS: Weight on L forearm, fully extends... |
| Q130 | - |  |  | SI | A. Lying & Rolling Dimension Score (%) |
| Q131 | - |  |  | SI | B. Sitting Dimension Score (%) |
| Q132 | - |  |  | SI | C. Crawling & Kneeling Dimension Score (%) |
| Q133 | - |  |  | SI | D. Standing Dimension Score (%) |
| Q134 | - |  |  | SI | E. Walking, Running & Jumping Dimension Score (%) |
| Q135 | - |  |  | SI | Chronological age |
| Q136 | - |  |  | SI | Age month |
| Q137 | - |  |  | SI | Age day |
| Q138 | - |  |  | SI | Y |
| Q139 | - |  |  | SI | M |
| Q14 | - |  |  | SI | PR: Rolls to SUP over R side |
| Q140 | - |  |  | SI | D |
| Q141 | - |  |  | SI | GMFCS Level |
| Q142 | - |  |  | SI | Date |
| Q143 | - |  |  | SI | Time |
| Q144 | - |  |  | SI | Total Score (%) |
| Q15 | - |  |  | SI | PR: Rolls to SUP over L side |
| Q16 | - |  |  | SI | PR: Pivots to R 90° using extremities |
| Q17 | - |  |  | SI | PR: Pivots to L 90°  using extremities |
| Q18 | - |  |  | SI | SUP, HANDS GRASPED BY EXAMINER: Pulls self to sitt... |
| Q19 | - |  |  | SI | SUP: Rolls to R side, attains sitting |
| Q20 | - |  |  | SI | SUP: Rolls to L side, attains sitting |
| Q21 | - |  |  | SI | SIT ON MAT, SUPPORTED AT THORAX BY THERAPIST: Lift... |
| Q22 | - |  |  | SI | SIT ON MAT, SUPPORTED AT THORAX BY THERAPIST: Lift... |
| Q23 | - |  |  | SI | SIT ON MAT, ARM(S) PROPPING: Maintains 5 seconds |
| Q24 | - |  |  | SI | SIT ON MAT: Maintain, arms free, 3 seconds |
| Q25 | - |  |  | SI | SIT ON MAT WITH SMALL TOY IN FRONT: Leans forward,... |
| Q26 | - |  |  | SI | SIT ON MAT: Touches toy placed 45°  behind child's... |
| Q27 | - |  |  | SI | SIT ON MAT: Touches toy placed 45° behind child's ... |
| Q28 | - |  |  | SI | R SIDE SIT: Maintains, arms free, 5 seconds |
| Q29 | - |  |  | SI | L SIDE SIT: Maintains, arms free, 5 seconds |
| Q30 | - |  |  | SI | SIT ON MAT: Lowers to PR with control |
| Q31 | - |  |  | SI | SIT ON MAT WITH FEET IN FRONT: Attains 4 points ov... |
| Q32 | - |  |  | SI | SIT ON MAT WITH FEET IN FRONT: Attains 4 points ov... |
| Q33 | - |  |  | SI | SIT ON MAT: Pivots 90°, without arms assisting |
| Q34 | - |  |  | SI | SIT ON BENCH: Maintains, arms and feet free, 10 se... |
| Q35 | - |  |  | SI | STD: Attains sit on small bench |
| Q36 | - |  |  | SI | ON THE FLOOR: Attains sit on small bench |
| Q37 | - |  |  | SI | ON THE FLOOR: Attains sit on large bench |
| Q38 | - |  |  | SI | PR: Creeps forward 1.8m (6') |
| Q39 | - |  |  | SI | 4 POINT: Maintains, weight on hands and knees, 10 ... |
| Q40 | - |  |  | SI | 4 POINT: Attains sit arms free |
| Q41 | - |  |  | SI | PR: Attains 4 point, weight on hands and knees |
| Q42 | - |  |  | SI | 4 POINT: Reaches forward with R arm, hand above sh... |
| Q43 | - |  |  | SI | 4 POINT: Reaches forward with L arm, hand above sh... |
| Q44 | - |  |  | SI | 4 POINT: Crawls or hitches forward 1.8m (6') |
| Q45 | - |  |  | SI | 4 POINT: Crawls reciprocally forward 1.8m (6') |
| Q46 | - |  |  | SI | 4 POINT: Crawls up 4 steps on hands and knees / fe... |
| Q47 | - |  |  | SI | 4 POINT: Crawls backwards down 4 steps on hands an... |
| Q48 | - |  |  | SI | SIT ON MAT: Attains high KN using arms, maintains,... |
| Q49 | - |  |  | SI | HIGH KN: Attains half KN on R knee using arms, mai... |
| Q50 | - |  |  | SI | HIGH KN: Attains half KN on L knee using arms, mai... |
| Q51 | - |  |  | SI | HIGH KN: KN walks forward 10 steps, arms free |
| Q52 | - |  |  | SI | ON THE FLOOR: Pulls to STD at large bench |
| Q53 | - |  |  | SI | STD: Maintains, arms free, 3 seconds |
| Q54 | - |  |  | SI | STD: Holding on to large bench with one hand, lift... |
| Q55 | - |  |  | SI | STD: Holding on to large bench with one hand, lift... |
| Q56 | - |  |  | SI | STD: Maintains, arms free, 20 seconds |
| Q57 | - |  |  | SI | STD: Lifts L foot, arms free, 10 seconds |
| Q58 | - |  |  | SI | STD: Lifts R foot, arms free, 10 seconds |
| Q59 | - |  |  | SI | SIT ON SMALL BENCH: Attains STD without using arms |
| Q60 | - |  |  | SI | HIGH KN: Attains STD through half KN on R knee, wi... |
| Q61 | - |  |  | SI | HIGH KN: Attains STD through half KN on L knee, wi... |
| Q62 | - |  |  | SI | STD: Lowers to sit on floor with control, arms fre... |
| Q63 | - |  |  | SI | STD: Attains squat, arms free |
| Q64 | - |  |  | SI | STD: Picks up object from floor, arms free, return... |
| Q65 | - |  |  | SI | STD, 2 HANDS ON LARGE BENCH: Cruises 5 steps to R |
| Q66 | - |  |  | SI | STD, 2 HANDS ON LARGE BENCH: Cruises 5 steps to L |
| Q67 | - |  |  | SI | STD, 2 HANDS HELD: Walks forward 10 steps |
| Q68 | - |  |  | SI | STD, 1 HAND HELD: Walks forward 10 steps |
| Q69 | - |  |  | SI | STD: Walks forward 10 steps |
| Q70 | - |  |  | SI | STD: Walks forward 10 steps, stops, turns 180°, re... |
| Q71 | - |  |  | SI | STD: Walks backwards 10 steps |
| Q72 | - |  |  | SI | STD: Walks forward 10 steps, carrying a large obje... |
| Q73 | - |  |  | SI | STD: Walks forward 10 consecutive steps between pa... |
| Q74 | - |  |  | SI | STD: Walks forward 10 consecutive steps on a strai... |
| Q75 | - |  |  | SI | STD: Steps over stick at knee level, R foot leadin... |
| Q76 | - |  |  | SI | STD: Steps over stick at knee level, L foot leadin... |
| Q77 | - |  |  | SI | STD: Runs 4.5m (15'), stops and returns |
| Q78 | - |  |  | SI | STD: Kicks ball with R foot |
| Q79 | - |  |  | SI | STD: Kicks ball with L foot |
| Q80 | - |  |  | SI | STD: Jumps 30cm (12) high, both feet simultaneousl... |
| Q81 | - |  |  | SI | STD: Jumps forward 30cm (12), both feet simultaneo... |
| Q82 | - |  |  | SI | STD ON R FOOT: Hops on R foot 10 times within a 60... |
| Q83 | - |  |  | SI | STD ON L FOOT: Hops on L foot 10 times within a 60... |
| Q84 | - |  |  | SI | STD, HOLDING 1 RAIL: Walks up 4 steps, holding 1 r... |
| Q85 | - |  |  | SI | STD, HOLDING 1 RAIL: Walks down 4 steps, holding 1... |
| Q86 | - |  |  | SI | STD: Walks up 4 steps, alternating feet |
| Q87 | - |  |  | SI | STD: Walks down 4 steps, alternating feet |
| Q88 | - |  |  | SI | STD ON 15cm (6) STEP: Jumps off, both feet simulta... |
| Q89 | - |  |  | SI | Date of Birth |
| Q90 | - |  |  | SI | Age at time of assessment |
| Q91 | - |  |  | SI | Testing condition (e.g., room, clothing, time, oth... |
| Q92 | - |  |  | SI | Was this assessment indicative of this child's 're... |
| Q93 | - |  |  | SI | Comments |
| Q94 | - |  |  | SI | The Gross Motor Function Measure (GMFM) is a stand... |
| Q95 | - |  |  | SI | 0 = does not initiate |
| Q96 | - |  |  | SI | 1 = initiates |
| Q97 | - |  |  | SI | 2 = partially completes |
| Q98 | - |  |  | SI | 3 = completes |
| Q99 | - |  |  | SI | NT = Not tested |
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
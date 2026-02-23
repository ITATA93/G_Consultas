# web_Msg.LB_StorageContainerPosition

**Schema:** web_Msg
**Columnas:** 22
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Laboratorio**. Módulo de laboratorio clínico.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| ID | varchar |  |  | NO | - |
| LBSTCP_Column | varchar |  |  | SI | Column
A label which identifies the column in the... |
| LBSTCP_Comment | varchar |  |  | SI | Comment |
| LBSTCP_ContentDesc | varchar |  |  | SI | Content Description |
| LBSTCP_DateChangeReason | varchar |  |  | SI | Date Change Reason |
| LBSTCP_DisposalDate | date |  |  | SI | Disposal Date |
| LBSTCP_NextReviewDate | date |  |  | SI | Next Review Date |
| LBSTCP_ParRef | bigint |  |  | SI | Parent Reference
Required by User.LBStorageContai... |
| LBSTCP_Position | varchar |  |  | SI | Position
A label which identifies the position in... |
| LBSTCP_ProtocolMaterial_DR | varchar |  | FK | SI | Protocol Material |
| LBSTCP_RequestBy_DR | bigint |  | FK | SI | Requested By DR |
| LBSTCP_ReserveForMaterial_DR | varchar |  | FK | SI | Reserve for Material |
| LBSTCP_ReviewCycle | numeric |  |  | SI | Review Cycle |
| LBSTCP_Row | varchar |  |  | SI | Row
A label which identifies the row in the conta... |
| LBSTCP_RowID | varchar |  |  | SI | - |
| LBSTCP_Sequence | numeric |  |  | SI | Sequence
Numeric value indicating the sequence in... |
| LBSTCP_SpecimenContainer_DR | bigint |  | FK | SI | Specimen Container DR |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
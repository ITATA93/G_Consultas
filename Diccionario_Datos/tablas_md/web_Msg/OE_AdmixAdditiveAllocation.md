# web_Msg.OE_AdmixAdditiveAllocation

**Schema:** web_Msg
**Columnas:** 13
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Componente Web**. Interfaz de usuario del sistema TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SessionParRef | varchar | PK |  | NO | - |
| AAA_Childsub | double |  |  | SI | Childsub |
| AAA_Form_DR | bigint |  | FK | SI | Des Ref to PHCForm |
| AAA_ItmMast_DR | varchar |  | FK | SI | Des Ref to ARCIM |
| AAA_ParRef | varchar |  |  | SI | OEAdmixAdditive Parent Reference
Required by User... |
| AAA_Quantity | double |  |  | SI | Quantity |
| AAA_RowId | varchar |  |  | SI | - |
| AAA_Strength_DR | bigint |  | FK | SI | Des Ref to PHCStrength |
| ID | varchar |  |  | NO | - |
| ReadOnly | bit |  |  | SI | - |
| SessionId | varchar |  |  | SI | - |
| childsub | bigint |  |  | NO | - |
| webMsgClassName | varchar |  |  | SI | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
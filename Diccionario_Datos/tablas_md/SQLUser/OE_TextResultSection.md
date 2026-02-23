# SQLUser.OE_TextResultSection

**Schema:** SQLUser
**Columnas:** 14
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

**Módulo del Sistema**. Componente interno de TrakCare.

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| SEC_ParRef | bigint | PK |  | NO | OE_TextResult Parent Reference |
| ChildQ47DR | - |  |  | SI | Child Reference: Special Test 1 (+ or - ) |
| Q46Q1 | - |  |  | SI | Muscle |
| Q46Q2 | - |  |  | SI | Strength left |
| Q46Q3 | - |  |  | SI | Strength right |
| Q46Q4 | - |  |  | SI | Resisted isometric test |
| QUESParRefDR | - |  |  | SI | Parent Reference |
| SEC_Childsub | double |  |  | NO | Childsub |
| SEC_HTMLPlainText | bigint |  |  | SI | Des Ref websys.Document |
| SEC_HTMLRichText | bigint |  |  | SI | Des Ref websys.Document |
| SEC_RTFText | varchar |  |  | SI | [DEPRECATED]Replaced by HTMLRichText control in Tr... |
| SEC_ResultTypeSection_DR | varchar |  | FK | SI | Des Ref ResultTypeSection |
| SEC_RowId | varchar |  |  | NO | - |
| SEC_Text | varchar |  |  | SI | Text |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
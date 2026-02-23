# questionnaire.QCLXXEXNEUQQ159

> Examen Neurológico y Físico : Agudeza Visual (Espec.)

**Schema:** questionnaire
**Columnas:** 9
**Actualizado:** 2026-01-30 15:29:54

## Utilidad

Tabla del sistema TrakCare.

*Descripción original:* Examen Neurológico y Físico : Agudeza Visual (Espec.)

## Columnas

| Columna | Tipo | PK | FK | Nullable | Descripcion |
|---------|------|----|----|----------|-------------|
| QUESParRefDR | bigint | PK | FK | NO | Parent Reference |
| ID | varchar |  |  | NO | - |
| Q159Q1 | varchar |  |  | SI | Uso de Lentes |
| Q159Q2 | varchar |  |  | SI | Ojo derecho (OD):  |
| Q159Q3 | varchar |  |  | SI | Ojo Izquierdo (OI):  |
| Q159Q4 | varchar |  |  | SI | CAE (OD):  |
| Q159Q5 | varchar |  |  | SI | CAE (OI):  |
| Q159Q6 | varchar |  |  | SI | Comentarios:  |
| childsub | bigint |  |  | NO | - |

---
*Generado: 2026-01-30 16:46 | Diccionario v1.0.0 | Sync: 2026-01-30 15:32:03*
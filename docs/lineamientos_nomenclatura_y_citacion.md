# Lineamientos de Nomenclatura y Citación
**Proyecto:** Agente Conversacional – Inteligencia Artificial (ITCR)

---

## 1. Estructura de nombres de archivo

**Formato oficial de nombre de archivo:**
```
<numeroSemana>_Semana_AI_<fechaYYYYMMDD>_<version>_<Autor>_<Tema>.pdf
```

**Ejemplo:**
```
6_Semana_AI_20250911_2_SahidRojasChacon_VerosimilitudRegresionLogistica.pdf
```

### 🔹 Reglas de nomenclatura
- Usar **guion bajo (`_`)** como separador.  
- No usar espacios, tildes ni caracteres especiales.  
- `numeroSemana`: coincide con la semana del curso (1–12).  
- `AI`: fijo, indica el curso de Inteligencia Artificial.  
- `fechaYYYYMMDD`: formato ISO sin guiones (ejemplo: `20250911`).  
- `version`: número incremental (`1`, `2`, `3`, etc.).  
- `Autor`: nombre y apellido sin tildes ni espacios (mayúscula inicial).  
- `Tema`: tema principal del apunte (breve y claro, máximo 5 palabras).  

### 🔹 Ejemplos válidos
| Correcto                                                                | Incorrecto                                         |
| `7_Semana_AI_20250918_1_DarioEspinoza_MetricasYDataCleaning.pdf`        | `Semana7 IA 18-09-25 Métricas y data cleaning.pdf` |
| `12_Semana_AI_20251023_2_LuisGonzalez_Quantization_RedesNeuronales.pdf` | `12 semana AI - Luis González Quantization.pdf`    |

---

## 🗂️ 2. Metadatos del inventario

El archivo oficial del inventario se encuentra en:  
```
/data/inventario/inventario_apuntes.xlsx
```

### 🔹 Columnas utilizadas
| Columna               | Descripción                                                                                  |
| **semana**            | Número de semana del curso (1–12).                                                           |
| **filename**          | Nombre exacto del archivo PDF en la carpeta `/apuntes_raw/`.                                 |
| **fecha_documento**   | Fecha del apunte (formato `YYYY-MM-DD`).                                                     |
| **version**           | Versión del documento (control de revisiones).                                               |
| **autor_principal**   | Nombre completo del estudiante autor del apunte.                                             |
| **tema_principal**    | Tema principal o título del documento.                                                       |
| **calidad_texto**     | Nivel de legibilidad del PDF: `ok`, `requiere_ocr` o `ilegible`.                             |
| **tiene_ecuaciones**  | Indica si el documento contiene fórmulas matemáticas (`sí`/`no`).                            |
| **estado_revision**   | Etapa de revisión del documento: `Pendiente`, `Revisado`, `A Procesar`, `Requiere Atención`. |

---

## 🧩 3. Reglas de citación de apuntes

Las citas se usarán en el informe final y en las respuestas del agente (RAG).

### 🔹 Formato corto (para respuestas del agente)
```
Fuente: <Autor> (<Año>), Semana <N> – <Tema principal>.
```
**Ejemplo:**  
> Fuente: Sahid Rojas (2025), Semana 6 – Verosimilitud en Regresión Logística.

### 🔹 Formato extendido (para el informe)
```
<Autor>. (Año). "<Tema principal>". Apunte de clase, Semana <N>. Curso Inteligencia Artificial, Instituto Tecnológico de Costa Rica.
```
**Ejemplo:**  
> Rojas Chacón, S. (2025). “Verosimilitud en regresión logística”. Apunte de clase, Semana 6. Curso Inteligencia Artificial, ITCR.

---

## 🧠 4. Estados de revisión (control de flujo)

| Estado                    | Significado                                            |
| 🟡 **Pendiente**         | Documento recién agregado, sin revisar.                |
| 🟠 **Revisando**         | En proceso de verificación de legibilidad y metadatos. |
| 🟢 **Revisado**          | Documento verificado y listo para análisis.            |
| 🔵 **A Procesar**        | Preparado para extracción de texto y embeddings.       |
| 🔴 **Requiere Atención** | Documento con errores (OCR, incompleto o duplicado).   |

---
